import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = 7279501
API_HASH = "fe8d3a7bb9b86fe1e58e02ed5a57cada"
SESSION = "migha"
HNDLR = "$"
SUDO_USERS = 5454772268
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
