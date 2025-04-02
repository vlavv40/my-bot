import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart  # Добавляем импорт

# Твой токен бота (замени на свой)
TOKEN = "8019699528:AAE1LebzllSYMZxoX8X3-oEvrc8xfz9i6zQ"

# Включаем логирование (для отладки)
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список фраз с эмоциональными выражениями и смайликами
responses = [
    "Еще 1 и я станцую для тебя танец маленьких утят 🐤",
    "о давай еще лидок, и я принесу тебе кофе в постель, но это не точно 😂",
    "ОГОНЬ 🔥 ",
    "🔥🔥🔥",
    "Тигра 🐅 ",
    "Танцую для тебя джигу-дрыгу 😏 ",
    "Бомба💣 ",
    "Можешь когда захочешь💉 ",
    "Зачет 😎 ",
    "Хух, ну хоть 1 есть 🤥 ",
    "Мощно 🤩 ",
    "Легенда ✨",
    "О,зашибись😍 ",
    "Ракета🚀‍",
    "В том же духе до 15 лидов💰 ",
    "Это по нашему, все берем пример и делаем так же ❤️‍",
    "Лояльная попалась 👀",
    "Ураааааааааааа! ❤️‍",
    "Сделаю на перекуре массаж пяток 🤝 ",
    "Еще один и идем с тобой вечером на свидание 💍",
    "Еще +1?‍😳",
    "Умничка моя 😘",
    "Чисто по красоте! обнимаю, целую, жму руку😍!"
]

# Важное сообщение для дублирования
important_message = "‼️Фитонормал и свампгель можно продавать ‼️\n\n" \
                    "3 оффера на подарок для курьера \n\n" \
                    "✅Вальготон (косточка на ноге)\n" \
                    "✅Венолид (варикоз)\n" \
                    "✅Мен сайз (потенция)"

# Переменная для хранения времени последнего дублирования
last_duplicate_time = 0

# Функция для дублирования важного сообщения
async def duplicate_message():
    global last_duplicate_time
    while True:
        current_time = asyncio.get_event_loop().time()
        if current_time - last_duplicate_time >= 3600:  # 3600 секунд = 1 час
            try:
                await bot.send_message(chat_id="-1001697395203", text=important_message)  # ID чата вставлен здесь
                last_duplicate_time = current_time
                logging.info("Важное сообщение продублировано.")
            except Exception as e:
                logging.error(f"Ошибка дублирования сообщения: {e}")
        await asyncio.sleep(60)  # Проверяем каждую минуту

# Обработчик сообщений
@dp.message()
async def respond(message: Message):
    if message.text in ["+1", "+2", "+1.5", "+1 кур", "+1 гум", "+1.5 гум", "+1 кросс"]:
        response = random.choice(responses)
        await message.reply(response)
        await message.react([types.ReactionTypeEmoji(emoji="❤️")])

@dp.message(CommandStart())  # Исправленная строка
async def start_command(message: types.Message):
    await message.reply("Привет! Я твой бот для продаж. Как дела?")

# Запуск бота и дублирование сообщений
async def main():
    asyncio.create_task(duplicate_message())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


