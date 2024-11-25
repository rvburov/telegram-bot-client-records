from fastapi import FastAPI, Request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создание FastAPI приложения
app = FastAPI()

# Создание Telegram приложения
telegram_app = Application.builder().token(BOT_TOKEN).build()

# Обработчик команды /start
async def handle_start_command(update: Update, context):
    keyboard = [[InlineKeyboardButton("Записаться", web_app=WebAppInfo(url="https://n698400.yclients.com/"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Выберите действие:", reply_markup=reply_markup)

# Регистрация обработчиков Telegram
telegram_app.add_handler(CommandHandler("start", handle_start_command))

# Асинхронная инициализация Telegram приложения
@app.on_event("startup")
async def startup_event():
    await telegram_app.initialize()
    print("Telegram application initialized")

@app.on_event("shutdown")
async def shutdown_event():
    await telegram_app.shutdown()

# Обработчик вебхуков
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}
