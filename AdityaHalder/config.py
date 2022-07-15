import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "12345678"))
API_HASH = getenv("API_HASH", "0ab1c2de3f4elf")
BOT_TOKEN = getenv("BOT_TOKEN", "5498692165:AAHEBZ_Ch0BW51erHnDNDbZJNqAWpnDQ-3Q")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
OWNER_ID = int(getenv("OWNER_ID", "5336023580"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001621569381"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/adityahalderxd/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
