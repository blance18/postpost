import telebot
import logging
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

# Загружаем .env переменные
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Пример команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Бот работает! 🔥")

# Планировщик
scheduler = BackgroundScheduler()

# Пример задачи по времени
def scheduled_job():
    bot.send_message(message.chat.id, "⏰ Запланированное сообщение!")

# scheduler.add_job(scheduled_job, 'interval', minutes=1)  # пример задачи
scheduler.start()

# Запуск бота
logger.info("Бот запущен!")
try:
    bot.infinity_polling()
except Exception as e:
    logger.error(f"Ошибка: {e}")