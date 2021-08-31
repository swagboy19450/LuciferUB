import time
from datetime import datetime
from io import BytesIO
import requests
from lucifer.plugins import PYTHON, OWNER_ID, LUCIFER
from lucifer import bot, vision, StartTime
from lucifer import CMD_HELP 
from lucifer.utils import admin_cmd, sudo_cmd
from lucifer.config import Config 
from telethon.errors import ChatSendInlineForbiddenError as king
from telethon.errors.rpcerrorlist import BotMethodInvalidError as barsh

# Configs #
botname = Config.BOT_USERNAME
NAME = Config.NAME
A_PIC = Config.A_PIC if Config.A_PIC else "https://telegra.ph/file/bc41c5a01e076dfc15293.mp4"
A_TEXT = Config.A_TEXT if Config.A_TEXT else " This is Lucifer\n   Ready in your protection"
emoji = "**❅**" 
emoji2 = "༺"
emoji3 = "༻"

# This is 4 later Purpose # 

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# uptime 
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
              remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
      
    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

start = datetime.now()

myid = bot.uid

    # By @Alone_loverBoy

end = datetime.now()

(end - start).microseconds / 1000

uptime = get_readable_time((time.time() - StartTime))

MYUSER = f"[{LUCIFER}](tg://user?id={OWNER_ID})"
lucifer = f"**『• Welcome To Lucifer •』**\n\n"
lucifer += f"**{A_TEXT}**\n\n"
lucifer += f"{emoji2}**iɲƒ๏ σƒ Lucifer**{emoji3}\n"
lucifer += f"{emoji}** Lucifer  Vision** ⊳≫ `{vision}`\n"
lucifer += f"{emoji}** Python Vision** ⊳≫  `{PYTHON}`\n"
lucifer += f"{emoji}** Lucifer uptime** ⊳≫ `{uptime}`\n"
lucifer += f"{emoji}** SUDO USER** ⊳≫ `{sudo}`\n"

lucifer += f"{emoji}** мy мαsтєя** ⊳≫ {MYUSER}\n\n"
lucifer += f"༆**✨Repository✨** ⊳≫ [GITHUB Repository✨](https://github.com/LuciferUB/LuciferUB)"

@bot.on(admin_cmd(pattern="alive"))
@bot.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
# ALONE #
    try:
        astro = await bot.inline_query(botname, "alive")
        await lucifer[0].click(alive.chat_id)
        if alive.sender_id == bot.uid:
            await alive.delete()
    except (king, barsh):
        await eor(alive, caption=lucifer)
    
CMD_HELP.update({"alive": "→ `.alive`\nUse - Check if your bot is working."})
 
# LUCIFER-UserBot
# © @Alone_loverboy
