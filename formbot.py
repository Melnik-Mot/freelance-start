import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8773954308:AAGbolghL18kPRdIQCwcgigJRN6CdtNeYhs"
ADMIN_ID = "2041222871"  # твой Telegram ID, чтобы получать ответы

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Словарь для хранения ответов пользователей
user_data = {}

questions = [
    "Как вас зовут?",
    "Сколько вам лет?",
    "Ваш город?",
    "Ваш e-mail?"
]

@dp.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {"answers": [], "current": 0}
    await message.answer(questions[0])

@dp.message()
async def questionnaire_handler(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        await message.answer("Начните с команды /start")
        return

    data = user_data[user_id]
    # Сохраняем ответ
    data["answers"].append(message.text)
    data["current"] += 1

    # Если вопросы не закончились
    if data["current"] < len(questions):
        await message.answer(questions[data["current"]])
    else:
        # Отправляем результаты админу
        answers_text = "\n".join(f"{q} {a}" for q, a in zip(questions, data["answers"]))
        await bot.send_message(ADMIN_ID, f"Новая анкета от {message.from_user.full_name}:\n{answers_text}")
        await message.answer("Спасибо! Ваша анкета отправлена.")
        # Очищаем данные
        user_data.pop(user_id)
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

