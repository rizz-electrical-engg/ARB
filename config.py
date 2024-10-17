import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21857983")
    API_HASH  = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7508789523:AAF7KkVdl_0ZT3EE7ruZycsvTtFcQ-YIxvo") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFNhr8AA0iYRR0DNYdwb-YFeHE_qA-hMi6-shX8BiFsNd-3AJLrFzLV3Gp5mdi7ZgnpOpcet-t6_Q4bn4AA4_ID8n03cmvfqg1xYoGWLMmsUQi1Wmn2kXTKqfE6hDbZ-K3Eaeat1r0krVmZQEvqLD9XPDo4MM_G8HOkMHMS3pWyPINZsBG34Bt5OIaPcmkhMjfeEllXnUs-JTXl5ovlR_OHgTgKPgXCO3SPgKys4iQda198RU_NwvcFAbAMcnbQnhnLOl5hRDR2d6s5Q-ZtQwMum9tMtEaqcVEhkADiQIAI69YhELdZV3NCOQLlf2AswHRYnvqILHs5pYm83ARskCNNshEUAAAAAAAxrasuAA")  # Set to None or a default value if not set
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/nxK.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '833465134').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'aboutRizzx').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002497860595"))
    PORT = int(os.environ.get("PORT", "60"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<blockquote expandable>Hello {} 
    
㊅ This Is An Advanced And Yet Powerful Rename Bot.
    
㊅ Using This Bot You Can Auto Rename Of Your Files.
    
㊅ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
<b>Bot Is Made By @ContactM_ebot</b></blockquote>"""
   
    FILE_NAME_TXT = """<blockquote expandable><b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>㊅ Example :</b> <code> /autorename  Naruto Shippuden S01[episode] [quality][Dual Audio] @aboutRizzx </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code></blockquote> """
    
    ABOUT_TXT = f"""<blockquote><b>
┏━━━━━━━━━━━━━
┣ 🔮 Creator        <a href='https://t.me/Noctophile'>𝙈𝙚</a>
┣ 🍄 Main Channel   <a href='https://t.me/aboutRizzx'>UPDATES </a>
┣ 🗿 Cloud Shop     <a href='https://t.me/vpsrdpdomainshop'>𝙑𝙋𝙎 | 𝗥𝗗𝗣 | 𝗗𝗼𝗺𝗮𝗶𝗻𝘀 ☁️</a>
┗━━━━━━━━━━━━━
</b></blockquote>"""

    
    THUMBNAIL_TXT = """<blockquote expandable><b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail</blockquote>"""

    CAPTION_TXT = """<blockquote expandable><b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption</blockquote>"""

    PROGRESS_BAR = """<blockquote>\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} </blockquote>"""
    
    
    DONATE_TXT = """<blockquote><b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>mehere@sbi</code></blockquote> """
    
    HELP_TXT = """<blockquote expandable><b>Hey</b> {}
    
Here Is The Help For My Commands.</blockquote>"""
    
    SEND_METADATA = """<blockquote expandable><b>📝  METADATA</b>
    
<b>➻ File Name :</b> <code>{filename}</code>
<b>➻ File Size :</b> <code>{filesize}</code>
<b>➻ File Type :</b> <code>{filetype}</code>
<b>➻ Duration :</b> <code>{duration}</code>
<b>➻ Resolution :</b> <code>{resolution}</code>
<b>➻ Frames :</b> <code>{frames}</code>
<b>➻ Bitrate :</b> <code>{bitrate}</code>
<b>➻ Audio Codec :</b> <code>{audio_codec}</code>
<b>➻ Video Codec :</b> <code>{video_codec}</code>
<b>➻ Fps :</b> <code>{fps}</code>
<b>➻ Aspect Ratio :</b> <code>{aspect_ratio}</code>
<b>➻ Rotation :</b> <code>{rotation}</code>
<b>➻ Bit Depth :</b> <code>{bit_depth}</code>
<b>➻ Scan Type :</b> <code>{scan_type}</code>
<b>➻ Interlaced :</b> <code>{interlaced}</code>
<b>➻ Top Field First :</b> <code>{top_field_first}</code>
<b>➻ Chroma Location :</b> <code>{chroma_location}</code>
<b>➻ Reel :</b> <code>{reel}</code>
<b>➻ Time Code :</b> <code>{time_code}</code>
<b>➻ Duration Ts :</b> <code>{duration_ts}</code>
<b>➻ Duration Ms :</b> <code>{duration_ms}</code>
<b>➻ Start Time :</b> <code>{start_time}</code>
<b>➻ End Time :</b> <code>{end_time}</code>
<b>➻ File Modified Date :</b> <code>{file_modified_date}</code>
<b>➻ File Creation Date :</b> <code>{file_creation_date}</code>
<b>➻ File Access Date :</b> <code>{file_access_date}</code>
<b>➻ File Inode Change Date :</b> <code>{file_inode_change_date}</code>
<b>➻ File Birth Time :</b> <code>{file_birth_time}</code>
<b>➻ File System Creation Time :</b> <code>{file_system_creation_time}</code>
<b>➻ File System Modification Time :</b> <code>{file_system_modification_time}</code>
<b>➻ File System Access Time :</b> <code>{file_system_access_time}</code>
<b>➻ File System Status Change Time :</b> <code>{file_system_status_change_time}</code>
<b>➻ File Birth Namespace :</b> <code>{file_birth_namespace}</code>
<b>➻ File System Id :</b> <code>{file_system_id}</code>
<b>➻ File System Device Id :</b> <code>{file_system_device_id}</code>
<b>➻ File System Flags :</b> <code>{file_system_flags}</code>
<b>➻ File System Block Size :</b> <code>{file_system_block_size}</code>
<b>➻ File System Block Count :</b> <code>{file_system_block_count}</code>
<b>➻ File System Available :</b> <code>{file_system_available}</code>
<b>➻ File System Total :</b> <code>{file_system_total}</code>
<b>➻ File System Used :</b> <code>{file_system_used}</code>
<b>➻ File System Free :</b> <code>{file_system_free}</code>
<b>➻ File System Percentage :</b> <code>{file_system_percentage}</code>
<b>➻ File System Mount Point :</b> <code>{file_system_mount_point}</code></blockquote>"""




