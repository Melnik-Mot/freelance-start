import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8747656943:AAEj5f7xuVzrqPu24YUucoYtN6Vjr-J_mCU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я калькулятор-бот 🤖\n"
                         "Просто пришли мне математическое выражение, например:\n"
                         "`2+2*3`")

@dp.message()
async def calculate(message: Message):
    lines = message.text.splitlines()  # Разделяем текст по строкам
    results = []
    for line in lines:
        try:
            result = eval(line)  # вычисляем каждую строку
            results.append(f"{line} = {result}")
        except Exception:
            results.append(f"{line} → ошибка!")
    await message.answer("\n".join(results))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
