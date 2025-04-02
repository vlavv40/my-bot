import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart  # Добавляем импорт
from datetime import datetime, timedelta

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

# Напоминание каждый день в 10:00
async def daily_reminder():
    while True:
        now = datetime.now()
        target_time = now.replace(hour=10, minute=0, second=0, microsecond=0)

        if now > target_time:
            target_time += timedelta(days=1)

        time_to_wait = (target_time - now).total_seconds()
        await asyncio.sleep(time_to_wait)  # Ожидаем до 10:00

        reminder_message = """‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️
КОНСУЛЬТАЦИЯ - 20 МИН В ДЕНЬ
ДОЗАПОЛНЕНИЕ - УЧИТЫВАЯ КУРЬЕРА 6 МИН НА ПРИНЯТЫЙ ЛИД
ОБУЧЕНИЕ - ТОЛЬКО ПО МОЕМУ. НАЗНАЧЕНИЮ
ЛИЧНЫЙ ПЕРЕРЫВ - 1 ЧАС
ЗВОНЮ В РУЧ - 15 МИН В ДЕНЬ
‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️

все перелимиты + 30 минут или штраф 100 грн 📌"""
        try:
            await bot.send_message(chat_id="-1001697395203", text=reminder_message)
            logging.info("Ежедневное напоминание отправлено.")
        except Exception as e:
            logging.error(f"Ошибка отправки ежедневного напоминания: {e}")

# Напоминание каждые 2 часа
async def hourly_reminder():
    while True:
        now = datetime.now()
        target_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=(now.hour // 2 + 1) * 2)

        time_to_wait = (target_time - now).total_seconds()
        await asyncio.sleep(time_to_wait)  # Ожидаем до следующего напоминания каждые 2 часа

        reminder_message = """🍄 Грибок ( свам экзостоп)
🍬Диабет (глюколикс)
🐛Паразиты (гетоксин,токсилид)
👣Вальгус (Вальготон и прочие)
🅱️Варикоз (Венсейв Венолид)
👂Слух (Лорабион)
🍆Увелечение (Титан Актив)

Вся гуманитарка (sharkfarmfree) и вот эти офферы проекта ФБ (sharkfarm) по старым ценам в к (4 уп) 1990 грн - (6 уп) 2844 грн"""
        try:
            await bot.send_message(chat_id="-1001697395203", text=reminder_message)
            logging.info("Напоминание через 2 часа отправлено.")
        except Exception as e:
            logging.error(f"Ошибка отправки напоминания через 2 часа: {e}")

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
    asyncio.create_task(daily_reminder())  # Добавляем задачу для ежедневного напоминания
    asyncio.create_task(hourly_reminder())  # Добавляем задачу для напоминаний каждые 2 часа
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

