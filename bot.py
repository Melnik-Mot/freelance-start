import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = 8666665014:AAEQbHOF-kZvno9PbzVZ2hlnVnATJrydvcs

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой первый бот 🤖")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
