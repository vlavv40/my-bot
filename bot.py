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

# 100 универсальных фраз
responses = [
    "ОГОНЬ 🔥", "🔥🔥🔥", "Тигра 🐅", "Танцую для тебя джигу-дрыгу 😏", "Бомба💣",
    "Можешь когда захочешь💉", "Зачет 😎", "Хух, ну хоть 1 есть 🤥", "Мощно 🤩", "Легенда ✨",
    "О, зашибись😍", "Ракета🚀", "В том же духе до 15 лидов💰", "Это по нашему! ❤️", "Лояльная попалась 👀",
    "Ураааааааааааа! ❤️", "Сделаю на перекуре массаж пяток 🤝", "Еще один и идем на свидание 💍",
    "Еще +1?‍😳", "Умничка моя 😘", "Чисто по красоте! обнимаю, целую, жму руку😍!", "Вижу прогресс! ✌️",
    "Ты машина 💪", "Заряжен на результат 🚀", "С каждым днем всё круче 🔥", "Босс продаж 💰",
    "Мастер своего дела 🎯", "Твой результат впечатляет 🏆", "Дай пять, чемпион 🖐️", "Феноменально! 😲",
    "Вот это уровень 😍", "Нереальный профи 🎖️", "Легенда в деле ✨", "Ангел продаж 😇",
    "Как же ты хорош(а) 😘", "Так держать! 🏆", "Пушка, ракета, ураган! 🚀🔥", "Ты просто зверь 🐺",
    "Золотые руки 💎", "Мастер звонков 🎤", "Бог торговли 🔱", "Я в шоке от твоего скилла 😱",
    "Так и до миллиона недалеко 💸", "Круче только Илон Маск 🚀", "Ты ходячий доллар 💲",
    "Прайс лист горит от твоих сделок 🔥", "Вот это клиентский сервис! 🏅", "Клиенты в восторге 🤩",
    "Ты на коне! 🐎", "Лидер по жизни! 👑", "Бро, ты лучший! 🤜🤛", "Как так можно продавать?! 🤯"
]

# Важные сообщения (раз в 3 часа)
important_messages = [
    """‼️Фитонормал и свампгель можно продавать ‼️
✅Вальготон (косточка на ноге)
✅Венолид (варикоз)
✅Мен сайз (потенция)""",
    
    """‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️
КОНСУЛЬТАЦИЯ - 20 МИН В ДЕНЬ
ДОЗАПОЛНЕНИЕ - 6 МИН НА ЛИД
ОБУЧЕНИЕ - ПО МОЕМУ НАЗНАЧЕНИЮ
ЛИЧНЫЙ ПЕРЕРЫВ - 1 ЧАС
ЗВОНЮ В РУЧ - 15 МИН В ДЕНЬ
‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️
Перелимиты +30 мин = штраф 100 грн 📌""",
    
    """🍄 Грибок (свам экзостоп) 
🍬 Диабет (глюколикс)  
🐛 Паразиты (гетоксин, токсилид) 
👣 Вальгус (Вальготон)  
🅱️ Варикоз (Венсейв Венолид) 
👂 Слух (Лорабион) 
🍆 Увелечение (Титан Актив) 
Вся гуманитарка по старым ценам (4 уп) 1990 грн - (6 уп) 2844 грн"""
]

# Функция для отправки всех важных сообщений раз в 3 часа
async def send_important_messages():
    while True:
        try:
            for msg in important_messages:
                await bot.send_message(chat_id="-1001697395203", text=msg)
                await asyncio.sleep(2)  # Чтобы не отправлять все сразу
            logging.info("Важные сообщения отправлены (повтор раз в 3 часа).")
        except Exception as e:
            logging.error(f"Ошибка отправки важных сообщений: {e}")
        
        await asyncio.sleep(10800)  # 3 часа (3 * 60 * 60 секунд)

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

# Запуск бота и фоновой задачи
async def main():
    asyncio.create_task(send_important_messages())  # Важные сообщения каждые 3 часа
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
