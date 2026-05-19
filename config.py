# 🗿  Visit & Support us - @UHD_NETWORK
# ⚡️ Do Not Remove Credit - Made by @UHDBots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")
API_ID = int(environ.get("API_ID", "32541562"))
API_HASH = environ.get("API_HASH", "e37e4432298d5a5eb4a6e32c18804283")
BOT_TOKEN = environ.get("BOT_TOKEN", "8932447404:AAHyanPJNFCm1yK7pA6hch2lnvMichi3qMI")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "")


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002521835919"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "2021145517").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://aaryansah954:QgDQRgyD7VUa7Eho@cluster0.wjo9zfm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "file")
