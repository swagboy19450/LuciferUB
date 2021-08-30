from lucifer.config import Config 
from lucifer import bot 
from lucifer import vision 
NAME = Config.NAME
OWNER_ID = Config.OWNER_ID
BOT_USERNAME = Config.BOT_USERNAME
OWNER_USERNAME = Config.OWNER_USERNAME
LUCIFER = "@Lucifer_support_group"
# Oh Yes...
if Config.SUDO_USERS:
    sudo = "YES Have Sudo"
else:
    sudo = "Nope No Sudo"
if Config.PMSECURITY.lower() == "off":
    pm = "DE-ACTIVE"
else:
    pm = "ACTIVE"

lucifer = f"Lucifer Vision: {vision}\n"
lucifer += f"SUDO USERS: {sudo}\n"
lucifer += f"PM SECURITY: {pm}\n"
lucifer += f"Assistant: {BOT_USERNAME}\n"
lucifer += f"My Master: {OWNER_USERNAME}\n"
lucifer += f"Protected by: {LUCIFER}\n\n"

luciferstats = f"{lucifer}"


# FOR PING LITTLE SETUP 
LUCIFER = bot.me.first_name
OWNER_ID = bot.me.id
NAAME = str(NAME) if NAME else "Lucifer User✨"

masteri = "𝐁𝐄𝐋𝐎𝐖 𝐈𝐒 𝐀𝐁𝐎𝐔𝐓 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑🥷\n\n"
masteri += f"USERNAME: {OWNER_USERNAME}\n"
masteri += f"ID: {OWNER_ID}\n"
masteri += f"NAME: {NAAME}\n"
masteri += "IS BOT: False\n"
masteri += f"Assistant: {BOT_USERNAME}\n\n"
masterinfo = f"{masteri}"

testro = "Hello This is About me😚\n"
testro += "Name: Lucifer υsєяъ๏т\n"
testro += f"Vision: {vision}\n"
testro += "Maintained🤔: Yes\n"
testro += "Gives Security: OP level\n"
testro += "Creator: @Murat_30_God\n\n"

aboutlucifer = f"{testro}"
# PYTHON VISION 
PYTHON = "3.9.6"
