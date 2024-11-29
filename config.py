



import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7075725841:AAEM_SSLJ4Inoe9161iylHbiVgHvXwaK98Q")
APP_ID = int(os.environ.get("APP_ID", "24371796"))
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")


OWNER = os.environ.get("OWNER", "God_Of_Genjutsue") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "5405110137")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "TA_Links_Bot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002149354979"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002177309175"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002146121321"))


SECONDS = int(os.getenv("SECONDS", "1200")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "👋🏻 Hey {mention}\n\nI Am Tamil Anime File Store Bot 🍀\nHere You Get All Tamil Animes @TA_Links🍂.")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "6076683960 7597065937").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot ! \n 👨‍💻 Contact Here : @TA_Links_Owner_Bot"

ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





