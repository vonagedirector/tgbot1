import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils import polling

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOTTOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    await message.answer("Бот работает! Вы написали: " + message.text)

async def bot_entrypoint():
    logging.basicConfig(level=logging.INFO)
    await polling(dp, bot)
