import asyncio
import logging
import random
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

# Твой токен бота
TOKEN = "8019699528:AAE1LebzllSYMZxoX8X3-oEvrc8xfz9i6zQ"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список фраз с эмоциональными выражениями и смайликами
responses = [
    "Еще 1 и я станцую для тебя танец маленьких утят 🐤",
    "О давай еще лидок, и я принесу тебе кофе в постель, но это не точно 😂",
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
    "О, зашибись😍 ",
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
important_message = """‼️Фитонормал и свампгель можно продавать ‼️

3 оффера на подарок для курьера 

✅Вальготон (косточка на ноге)
✅Венолид (варикоз)
✅Мен сайз (потенция)"""

# Напоминание, отправляемое в 10:00 утра
morning_message = """‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️
КОНСУЛЬТАЦИЯ - 20 МИН В ДЕНЬ
ДОЗАПОЛНЕНИЕ - УЧИТЫВАЯ КУРЬЕРА 6 МИН НА ПРИНЯТЫЙ ЛИД
ОБУЧЕНИЕ - ТОЛЬКО ПО МОЕМУ НАЗНАЧЕНИЮ
ЛИЧНЫЙ ПЕРЕРЫВ - 1 ЧАС
ЗВОНЮ В РУЧ - 15 МИН В ДЕНЬ
‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️

Все перелимиты + 30 минут или штраф 100 грн 📌"""

# Ежечасное напоминание
hourly_message = """🍄 Грибок (свам экзостоп) 
🍬 Диабет (глюколикс)  
🐛 Паразиты (гетоксин, токсилид) 
👣 Вальгус (Вальготон и прочие)  
🅱️ Варикоз (Венсейв Венолид) 
👂 Слух (Лорабион) 
🍆 Увелечение (Титан Актив) 

Вся гуманитарка (sharkfarmfree) и вот эти офферы проекта ФБ (sharkfarm) по старым ценам:
(4 уп) 1990 грн - (6 уп) 2844 грн"""

# Переменная для хранения времени последнего дублирования
last_duplicate_time = 0

# Функция для дублирования важного сообщения
async def duplicate_message():
    global last_duplicate_time
    while True:
        current_time = asyncio.get_event_loop().time()
        if current_time - last_duplicate_time >= 3600:  # 3600 секунд = 1 час
            try:
                await bot.send_message(chat_id="-1001697395203", text=important_message)  
                last_duplicate_time = current_time
                logging.info("Важное сообщение продублировано.")
            except Exception as e:
                logging.error(f"Ошибка дублирования сообщения: {e}")
        await asyncio.sleep(60)  # Проверяем каждую минуту

# Функция для отправки напоминания в 10:00 утра
async def daily_morning_reminder():
    while True:
        now = datetime.datetime.now()
        target_time = now.replace(hour=10, minute=0, second=0, microsecond=0)

        # Если уже после 10:00, устанавливаем цель на следующий день
        if now > target_time:
            target_time += datetime.timedelta(days=1)

        wait_time = (target_time - now).total_seconds()
        logging.info(f"Ждем {wait_time / 3600:.2f} часов до утреннего напоминания...")
        await asyncio.sleep(wait_time)

        try:
            await bot.send_message(chat_id="-1001697395203", text=morning_message)
            logging.info("Утреннее напоминание отправлено.")
        except Exception as e:
            logging.error(f"Ошибка отправки утреннего напоминания: {e}")

# Функция для отправки напоминания каждый час
async def hourly_reminder():
    while True:
        await asyncio.sleep(3600)  # Ждем 1 час
        try:
            await bot.send_message(chat_id="-1001697395203", text=hourly_message)
            logging.info("Ежечасное напоминание отправлено.")
        except Exception as e:
            logging.error(f"Ошибка отправки ежечасного напоминания: {e}")

# Обработчик сообщений
@dp.message()
async def respond(message: Message):
    if message.text in ["+1", "+2", "+1.5", "+1 кур", "+1 гум", "+1.5 гум", "+1 кросс"]:
        response = random.choice(responses)
        await message.reply(response)
        await message.react([types.ReactionTypeEmoji(emoji="❤️")])

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.reply("Привет! Я твой бот для продаж. Как дела?")

# Запуск бота и фоновых задач
async def main():
    asyncio.create_task(duplicate_message())       # Дублирование важного сообщения
    asyncio.create_task(daily_morning_reminder())  # Утреннее напоминание в 10:00
    asyncio.create_task(hourly_reminder())         # Ежечасное напоминание
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
