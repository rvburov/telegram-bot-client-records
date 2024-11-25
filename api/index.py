from fastapi import FastAPI, Request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from fastapi.responses import JSONResponse
from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv
import uvloop
import asyncio

# Установить uvloop для asyncio
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

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

# Обработчик ошибок Telegram
async def error_handler(update, context):
    print(f"Update {update} caused error {context.error}")

telegram_app.add_error_handler(error_handler)

# Инициализация Telegram приложения
asyncio.run(telegram_app.initialize())

# Обработчик вебхуков
@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        update = Update.de_json(data, telegram_app.bot)
        await telegram_app.process_update(update)
        return {"status": "ok"}
    except Exception as e:
        print(f"Error in webhook: {e}")
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)

@app.get("/")
async def root():
    return {"message": "Hello from Vercel"}
