import time 
from datetime import datetime 
from lucifer import bot
from lucifer.plugins import LUCIFER, OWNER_ID
from lucifer.config import Config 
### Config ### 
 

@astro.on(admin_cmd(pattern=r"ping$"))
@astro.on(sudo_cmd(pattern=r"ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "β’ππππβ’")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
PONG
βββmy ms β£ `{ms}s` β β \n
|β ny ownerβ’ [{LUCIFER}](tg://user?id={OWNER_ID}) β|
 \n
 ~ LUCIFER ΟsΡΡΡΰΉΡ ~
""")
# Β© @Alone_loverboy 
# FOR OWN ASTRO UserBot
#now in Lucifer userbot
