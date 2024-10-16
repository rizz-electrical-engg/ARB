from pyrogram import Client, filters
from pyrogram.types import Message
import re
import asyncio
from helper.database import AshutoshGoswami24
from helper.utils import progress_for_pyrogram, humanbytes, convert
from config import Config
import os
import time

# Queue to store pending rename operations
user_queues = {}
# Queue for files ready to be uploaded
upload_queues = {}
# Set to keep track of files currently being downloaded
downloading_files = set()
# Maximum number of concurrent downloads
MAX_CONCURRENT_DOWNLOADS = 3

async def add_to_queue(user_id, message):
    if user_id not in user_queues:
        user_queues[user_id] = []
    user_queues[user_id].append(message)

async def get_next_in_queue(user_id):
    if user_id in user_queues and user_queues[user_id]:
        return user_queues[user_id].pop(0)
    return None

def extract_episode_number(filename):
    patterns = [
        re.compile(r"S(\d+)(?:E|EP)(\d+)"),
        re.compile(r"S(\d+)\s*(?:E|EP|-\s*EP)(\d+)"),
        re.compile(r"(?:[([<{]?\s*(?:E|EP)\s*(\d+)\s*[)\]>]?"),
        re.compile(r"(?:\s*-\s*(\d+)\s*)"),
        re.compile(r"S(\d+)[^\d]*(\d+)", re.IGNORECASE),
        re.compile(r"(\d+)")
    ]
    
    for pattern in patterns:
        match = pattern.search(filename)
        if match:
            if len(match.groups()) > 1:
                return int(match.group(2))
            return int(match.group(1))
    
    return 9999  # Default high number for files without episode number

@Client.on_message(filters.private & filters.command(["queuerememe", "qr", "addtoqueue", "aq"]))
async def queue_rename(client, message):
    user_id = message.from_user.id
    
    if message.reply_to_message:
        await add_to_queue(user_id, message.reply_to_message)
        queue_size = len(user_queues[user_id])
        await message.reply_text(f"File added to queue. Current queue size: {queue_size}")
    else:
        await message.reply_text("Please reply to a file with this command.")
    
    if len(downloading_files) < MAX_CONCURRENT_DOWNLOADS:
        asyncio.create_task(process_download_queue(client, user_id))
    
    # Start the upload process if it's not already running
    if user_id not in upload_queues:
        upload_queues[user_id] = asyncio.Queue()
        asyncio.create_task(process_upload_queue(client, user_id))

async def process_download_queue(client, user_id):
    while True:
        if len(downloading_files) >= MAX_CONCURRENT_DOWNLOADS:
            await asyncio.sleep(1)
            continue
        
        message = await get_next_in_queue(user_id)
        if not message:
            break
        
        file_id = f"{user_id}_{message.id}"
        if file_id in downloading_files:
            continue
        
        downloading_files.add(file_id)
        asyncio.create_task(download_and_rename_file(client, message, file_id, user_id))
    
    if not user_queues[user_id] and not downloading_files:
        await client.send_message(user_id, "All files have been downloaded and renamed.")

async def download_and_rename_file(client, message, file_id, user_id):
    try:
        file_path = await client.download_media(message, progress=progress_for_pyrogram, progress_args=("Downloading...", message, ""))
        
        # Extract episode number from filename
        episode_number = extract_episode_number(os.path.basename(file_path))
        
        # Rename the file
        new_filename = f"Episode {episode_number}.mp4"
        os.rename(file_path, new_filename)
        
        # Add to upload queue
        if user_id not in upload_queues:
            upload_queues[user_id] = asyncio.Queue()
        await upload_queues[user_id].put(new_filename)
    finally:
        downloading_files.remove(file_id)

async def process_upload_queue(client, user_id):
    while True:
        file_path = await upload_queues[user_id].get()
        files_to_upload = [file_path]
        
        # Wait for all files to be added to the queue before uploading
        while not upload_queues[user_id].empty():
            file_path = await upload_queues[user_id].get()
            files_to_upload.append(file_path)
        
        # Sort files by episode number
        files_to_upload.sort(key=lambda x: extract_episode_number(os.path.basename(x)))
        
        # Upload the files
        for file_path in files_to_upload:
            await client.send_video(user_id, file_path, caption=os.path.basename(file_path), progress=progress_for_pyrogram, progress_args=("Uploading...", file_path, ""))
        
        # Clear the queue and mark task as done
        upload_queues[user_id].task_done()
        files_to_upload.clear()
