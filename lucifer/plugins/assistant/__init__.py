from lucifer.plugins import LUCIFER, OWNER_ID
import time
from datetime import datetime
from lucifer.config import Config 

# OTHER STARTED WHILE DISABLE BOT 
others = """
Hi there. I am {}'s bot. Nice to see you here
""".format(LUCIFER)
# Ok you know 

if Config.PMBOT_START_MSSG is None:
    MSSG = """
Hi there, I am {}'s personal bot.
I am Helper BoT 😁
Contact him from me Just send me Your Message 😌 I will forward him 
""".format(LUCIFER)
else:
    MSSG = Config.PMBOT_START_MSSG
customtxt = MSSG

ownerstart = """
Hi {} How are you master 
select What can i do for You Today😁
""".format(LUCIFER)
