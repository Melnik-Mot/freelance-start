import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "8044494973:AAHkoHI8yI50OMSd5ufr8UX9tQ1xptmb8ao"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаём клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Услуги")],
        [KeyboardButton(text="Контакты")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Выберите кнопку ниже 👇", reply_markup=keyboard)

# Обработчик нажатий кнопок
@dp.message()
async def button_handler(message: Message):
    if message.text == "О нас":
        await message.answer("Мы – команда по разработке ботов 🤖")
    elif message.text == "Услуги":
        await message.answer("Мы создаём ботов, веб-приложения и автоматизации")
    elif message.text == "Контакты":
        await message.answer("Пишите нам: example@mail.com")
    else:
        await message.answer("Пожалуйста, выберите кнопку из меню")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
