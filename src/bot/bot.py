import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOTTOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Бот работает! Вы написали: {message.text}")

async def bot_entrypoint():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
