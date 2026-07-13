import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
import logging
import logging.config
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait

# logging setup
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            "AutoForwardBot",  # Session name
            api_id=int(os.getenv("36739180")),
            api_hash=os.getenv("a4974292591c16f7d28ad09c16501f9c"),
            bot_token=os.getenv("8697819852:AAH9xXxO-yFDve6hIWwPhV1_paGG8EsL0p0"),
            plugins={"root": "plugins"},
            workers=50,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        print(f"✅ Bot Started! | Pyrogram v{__version__} | Layer: {layer}")
        print("🤖 Auto Forward Bot is Ready...")

    async def stop(self):
        await super().stop()
        print("⛔ Bot Stopped")

# Environment Variable Import
import os
from dotenv import load_dotenv
load_dotenv()