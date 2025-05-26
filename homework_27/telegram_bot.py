import logging
import pika
import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
import load_dotenv

# === Налаштування ===
load_dotenv() #
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DJANGO_BACKEND_URL = os.getenv('DJANGO_BACKEND_URL')

# === Вивід логів ===
logging.basicConfig(level=logging.INFO)

# === Функція обробки /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Надішли мені своє ім'я та email через кому (наприклад: Ivan, ivan@example.com)")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        name, email = map(str.strip, text.split(","))
        payload = {"username": name, "email": email}

        # Надсилання даних у Django
        resp = requests.post(DJANGO_BACKEND_URL, json=payload)
        if resp.status_code == 200:
            await update.message.reply_text("Тебе зареєстровано!")
        else:
            await update.message.reply_text("Помилка при реєстрації :(")
    except Exception as e:
        await update.message.reply_text("Неправильний формат. Введи ім'я та email через кому.")

# === Запуск Telegram бота ===
def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()

# === Запуск слухача RabbitMQ для отримання повідомлень від Django ===
def callback(ch, method, properties, body):
    data = json.loads(body)
    message = f"Новий користувач: {data.get('name')} ({data.get('email')})"
    # Тут можна було б зберігати chat_id і надсилати повідомлення користувачу
    print("[Bot] ✉️ Новий користувач зареєстрований:", message)

def start_rabbit_listener():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost",port=5672))
    channel = connection.channel()
    channel.exchange_declare(exchange='events', exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='events', queue=queue_name, routing_key="user.registered")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print("[Bot] 🔊 Listening for user.registered events...")
    channel.start_consuming()

# === Запуск обох процесів (приклад для окремого запуску) ===
if __name__ == "__main__":
    from threading import Thread
    Thread(target=start_rabbit_listener, daemon=True).start()
    run_bot()

