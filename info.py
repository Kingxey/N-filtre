import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24817837'))
API_HASH = environ.get('API_HASH', 'acd9f0cc6beb08ce59383cf250052686') 
BOT_TOKEN = environ.get('BOT_TOKEN', '7606613494:AAHc-vHZ0fW4PKHuIeIATWRwfEX63NsAGGY') 

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS' ,'https://i.ibb.co/N2vwCj9h/file-659.jpg https://i.ibb.co/F4RtNCzt/6a06fe6a-beea-45b6-a91b-729054c1fa4b.jpg https://i.ibb.co/rKByHQ6s/ef932da8-4d55-40d8-9117-e3dc0e8e75b9.jpg https://i.ibb.co/G3NNB4JY/1ff6aa3b-9f64-4b87-a072-94d1204b70d2.jpg https://i.ibb.co/Z1YmGwvc/09f6409c-466c-4bcd-b791-cb5e3fcf037e.jpg https://i.ibb.co/399ntZMj/8bfd1763-3183-4f45-893e-30a1fec5042d.jpg')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 800)) 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5814104129 7428552084 kingcey').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7428552084 1687928453').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002647818964')
auth_grp = environ.get('AUTH_GROUP', '-1002427882015')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
# MongoDB information
DATABASE_URI = environ.get('DATABASE_URL', "mongodb+srv://altof2:123Bonjoure@cluster0.s1suq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "bot")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URI)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', '🌺 𝒉𝒆𝒍𝒍𝒐 {user}\n\n𝒎𝒚 𝒏𝒂𝒎𝒆 𝒊𝒔 {bot},\n\n𝒊 𝒄𝒂𝒏 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒎𝒐𝒗𝒊𝒆𝒔, 𝒋𝒖𝒔𝒕 𝒂𝒅𝒅 𝒎𝒆 𝒕𝒐 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑 𝒂𝒏𝒅 𝒎𝒂𝒌𝒆 𝒎𝒆 𝒂𝒅𝒎𝒊𝒏...  ')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "❖ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', 'Yo mon pôte. Pour récupéré ta requête, tu dois d'abord rejoindre mes canaux @KGCAnime & @BotZFlix pour utilisé également mes fonctionnalités!')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "🎥 Salut, {user} !\nBienvenue dans *{chat}* – votre guichet unique pour tout ce qui est séries et films !\nJe suis là pour vous servir. Envoyez-moi simplement un titre, et je m'occupe du reste. 🍿\nPlongez dans l'univers du divertissement et profitez de contenus soigneusement sélectionnés pour vous !")
PMFILTER = environ.get('PMFILTER', "True")
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = environ.get("BUTTON_LOCK", "True")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "900"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002376378205))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'BotZFlixSupport')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = environ.get('PM_IMDB', "True")
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name} @KGCAnime & @ZFlixTeam")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Demande: {query}</b> \n‌IMDb Data:\n\n❖ Titre: <a href={url}>{title}</a>\n❖ Genres: {genres}\n❖ Année: <a href={url}/releaseinfo>{year}</a>\n❖ Rang: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002202721408')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#request force sub
REQ_SUB = bool(environ.get("REQ_SUB", True))
SESSION_STRING = environ.get("SESSION_STRING", "Hokageclub")








