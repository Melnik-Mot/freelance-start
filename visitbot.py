import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandStart

TOKEN = "8786079577:AAE4A35qvLf-EBQDzpr4Acwqd80BxBBRRJE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# создаём кнопки
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📄 Услуги"), KeyboardButton(text="💰 Цена")],
        [KeyboardButton(text="📞 Контакты"),KeyboardButton(text="Кто ты?")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Выбери пункт меню 👇", reply_markup=kb)

@dp.message()
async def handle_buttons(message: Message):
    if message.text.startswith("/"):
        return

    text = message.text

    if text == "📄 Услуги":
        await message.answer("Я делаю Telegram-ботов, автоматизацию и парсинг 🔥")

    elif text == "💰 Цена":
        await message.answer("От 1000 до 5000 рублей в зависимости от задачи")

    elif text == "📞 Контакты":
        await message.answer("Напиши мне: @your_username")
    
    elif text == "Кто ты?":
        await message.answer("Я бот, которого написал начинающий разработчик")

    else:
        await message.answer("Выбери кнопку 👇")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

