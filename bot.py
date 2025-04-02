import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Список фраз с эмоциональными выражениями и смайликами для парней
responses_male = [
    "Тигр 🐅", "Бро, лучший! Давай 5 🙌", "Выпьем пивка с тобой после 6 🍻", 
    "Жму лапу, бро 👊", "Обнимаю, братишка 🤗", "Мощно, брат! 😎", 
    "Точно по делу, молодец! 💪", "Тебе респект, братан! ✊", "В огонь пошел, брат 🔥", 
    "Вот это стиль, да! 👌", "Ты настоящий лидер, брат! 👑", "Давай так и дальше, бро! 🚀", 
    "Респект тебе, чувак! ✌️", "Поехали дальше, не останавливайся! 🏎️", "Ты лучший в деле! 🎯", 
    "Зачет, вот это подход! ✅", "Ты вообще красава, брат! 🌟", "Никаких тормозов, давай в топ! 🏁", 
    "Ты как боец, не сдаешься! 🥊", "Ты в топе, брат! 🏆", "Круто, что ты в команде! 🤝", 
    "Давай так и дальше, не останавливаться! 🔥", "Ты реально тащишь, братан! 💥", "Все по кайфу, продолжаем! 😎", 
    "Ты просто топчик, бро! 🔝", "Бери пример с меня, брат! 📚", "Молодец, вот так держать! 💪"
]

# Список фраз с эмоциональными выражениями и смайликами для девушек
responses_female = [
    "Красотка, в том же духе! 💖", "Умница, продолжаем в том же духе! ✨", "Молодчина, ты просто супер! 😍", 
    "Ты реально крутая! 💅", "Давай так и дальше, красотка! 💕", "Ты просто огонь! 🔥", 
    "Отличная работа, молодец! 🌟", "Красавица, продолжаем в том же духе! 💫", "Ты — настоящая звезда! ⭐", 
    "В этом нет сомнений, ты лучший! 💪", "Ты такая яркая, прям светишься! ✨", "Ты пример для подражания! 🌟", 
    "Вот так держать, красавица! 💃", "Продолжаем работать на результат! 🚀", "Ты просто шикарна, ура! 🎉", 
    "Ты как алмаз, сверкаешь! 💎", "Ты в топе, не останавливайся! 🏆", "С каждым шагом ты всё круче! 👏", 
    "Красотка, не останавливайся! 🌸", "Ты — это настоящий пример! 💪", "Ты как фея, волшебная! 🧚‍♀️", 
    "Ты — супер, не правда ли? 😘", "Давай, продолжай в том же духе! 💪", "Ты потрясающая, не останавливайся! 🏅", 
    "Ты одна из лучших! 🌟", "Ты просто чудо, умничка! 😍", "Ты всегда на высоте, красавица! 👑"
]

# Хранилище пола пользователя
user_genders = {}

# Функция для получения приветствия в зависимости от пола
def get_greeting(user_gender):
    if user_gender == "male":
        return random.choice(responses_male)
    elif user_gender == "female":
        return random.choice(responses_female)
    else:
        return "Привет!"

# Функция для установки пола пользователя
def set_gender(update: Update, context: CallbackContext):
    user = update.message.from_user
    gender = update.message.text.split(' ')[1].lower()  # Ожидаем, что пользователь введет команду вида "/set_gender male" или "/set_gender female"
    
    if gender not in ['male', 'female']:
        update.message.reply_text("Пожалуйста, используйте /set_gender male или /set_gender female")
        return
    
    user_genders[user.id] = gender
    update.message.reply_text(f"Пол успешно установлен: {gender.capitalize()}!")

# Функция обработки команды "/start"
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    gender = user_genders.get(user.id, None)
    
    if gender is None:
        update.message.reply_text("Пожалуйста, установите ваш пол с помощью команды /set_gender.")
        return
    
    greeting = get_greeting(gender)
    update.message.reply_text(greeting)

# Создание и запуск бота
def main():
    # Используем свой токен, полученный от BotFather
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("set_gender", set_gender))
    dispatcher.add_handler(MessageHandler(Filters.text, start))  # Для всех текстовых сообщений

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
