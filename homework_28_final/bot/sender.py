import asyncio
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))
bot = Bot(token=TOKEN)

async def send_alert(message: str):
   await bot.send_message(chat_id=ADMIN_USER_ID, text=message)

if __name__ == "__main__":
   asyncio.run(send_alert("🚨 CPU  !!!!"))

