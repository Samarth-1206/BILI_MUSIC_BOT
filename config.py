import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("25172549"))
API_HASH = getenv("b04878ffbf15cb5dd08ea72ae7067e16")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7561897338:AAFCipEiTLts3BMiZUO8dHyJeBBeGF-NLt4")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","ixigio")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "Bili_Music_bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "˹𝐁ɪʟɪ ꭙ 𝐌ᴜsɪᴄ˼ [ ɴᴏ ᴀᴅʂ ]")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "˹ＮＯＯＲ ꭙ ᴧssɪsᴛᴧηᴛ˼")
EVALOP = list(map(int, getenv("EVALOP", "7316175278").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002669019123", ))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("6311318596", ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
   "UPSTREAM_REPO",
   "https://github.com/MISH0009/MishuXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
   "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GHOULS_NETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GHOULS_SUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", BQGAGkUAt7KwLoadYbewdo7UPSBNpFnm6NmQFOJaAgEZTRC_yoSPe-RT3764-cuWIn-AG_6q2zYdy11_hpHobde-4X9GrP9s6yHSftKvv0sj2eAOa2XD9EaO1KmTm_u9Ixpuqgwnk_Z87q57vSMBcX_hDAsDekPKl4WJH4ixunw_V2gicy8FT6z27ogzkPI9q32CMVFw0SEKmRVBd8XVoB6yZTh_Qubji7sZtD1IZTCSo4LwWwbtXvE_1BBr16uJJMX4a_SuQW96cbxYZpNkvvcGjRSNDDnCmBklt1o__zSBibXh1Ce1loSSa4gqEmmQCUEi4G7sz2SNGgID3X20jt29kznvIwAAAAG0E_muAA )
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
   "START_IMG_URL", "https://files.catbox.moe/2t62vg.jpg"
)
PING_IMG_URL = getenv(
   "PING_IMG_URL", "https://files.catbox.moe/yyc0e8.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/5yfzv2.jpg"
STATS_IMG_URL = "https://files.catbox.moe/5pkn9k.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/v2wc0z.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/v2wc0z.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/v2wc0z.jpg"


def time_to_seconds(time):
   stringt = str(time)
   return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
   if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
       raise SystemExit(
       "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
       )
       
if SUPPORT_CHAT:
   if not re.match("(?:http|https)://", SUPPORT_CHAT):
       raise SystemExit(
           "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
       )
