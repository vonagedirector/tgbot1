import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.runner import run_polling
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOTTOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    await message.answer("Бот работает! Вы написали: " + message.text)

async def bot_entrypoint():
    logging.basicConfig(level=logging.INFO)
    await run_polling(dispatcher=dp, bot=bot)
