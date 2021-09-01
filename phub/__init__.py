from os import environ as e
from telethon import TelegramClient 

API_KEY = e.get("API_KEY")
API_HASH = e.get("API_HASH")
TOKEN = e.get("TOKEN")
OWNERS = list(e.get("OWNERS").split(' '))

bot = TelegramClient('phub', API_KEY, API_HASH)

