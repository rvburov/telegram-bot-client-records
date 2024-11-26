from fastapi import FastAPI, Request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv
import asyncio

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создание FastAPI приложения
app = FastAPI()

# Создание и инициализация Telegram приложения
telegram_app = Application.builder().token(BOT_TOKEN).build()
bot = Bot(token=BOT_TOKEN)  # Инициализация бота для установки команд
asyncio.run(telegram_app.initialize())

# Устанавливаем команды для меню
async def set_bot_commands():
    commands = [
        BotCommand("start", "Запустить бота"),
        BotCommand("contact", "Контакты")
    ]
    await bot.set_my_commands(commands)

# Отправляем сообщение с фото, текстом и кнопками
async def handle_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text == "/start":
        keyboard = [
            [InlineKeyboardButton("Записаться", web_app=WebAppInfo(url="https://n698400.yclients.com/"))],
            [InlineKeyboardButton("Продукция для бритья", callback_data="shaving_products")],
            [InlineKeyboardButton("Проложить маршрут к нам", url="https://yandex.ru/navi/org/buldog_barbershop/228670617679?si=53tdhmrm859cg5xgwpeu0hng6r")],
            [InlineKeyboardButton("⭐️ Оставить отзыв ⭐️", web_app=WebAppInfo(url="https://yandex.ru/maps/org/barberman/221541041982/reviews/?ll=30.320363%2C59.886241&mode=search&sll=30.320363%2C59.886239&tab=reviews&text=%22Россия%2C%20Санкт-Петербург%2C%20Московский%20проспект%2C%20140%2C%20Barberman%22&z=14"))],
            [InlineKeyboardButton("Instagram", web_app=WebAppInfo(url="https://instagram.com/your_instagram"))],
            [InlineKeyboardButton("VK", web_app=WebAppInfo(url="https://m.vk.com/barbermanspb"))],
            [InlineKeyboardButton("Написать сообщение", url="https://t.me/BARBERMANSPB")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Отправляем изображение
        await update.message.reply_photo(
            photo="https://avatars.mds.yandex.net/get-altay/5476806/2a0000017e6a21f86297a5246460c10df452/XXXL",
            caption="⬇️ Привет! Выберите действие ⬇️",
            reply_markup=reply_markup
        )

# Обрабатываем кнопку "Продукция для бритья"
async def handle_shaving_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем новое сообщение с текстом и кнопками
    await update.callback_query.message.reply_text(
        "Продукция для бритья:\n"
        "1. Кремы для бритья\n"
        "2. Лосьоны после бритья\n"
        "3. Бритвы и аксессуары\n"
        "4. Пены для бритья\n"
        "5. Масла и бальзамы после бритья",
        reply_markup=reply_markup
    )

# Возврат в главное меню
async def handle_back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Записаться", web_app=WebAppInfo(url="https://n698400.yclients.com/"))],
        [InlineKeyboardButton("Продукция для бритья", callback_data="shaving_products")],
        [InlineKeyboardButton("Проложить маршрут к нам", url="https://yandex.ru/navi/org/buldog_barbershop/228670617679?si=53tdhmrm859cg5xgwpeu0hng6r")],
        [InlineKeyboardButton("⭐️ Оставить отзыв ⭐️", web_app=WebAppInfo(url="https://yandex.ru/maps/org/barberman/221541041982/reviews/?ll=30.320363%2C59.886241&mode=search&sll=30.320363%2C59.886239&tab=reviews&text=%22Россия%2C%20Санкт-Петербург%2C%20Московский%20проспект%2C%20140%2C%20Barberman%22&z=14"))],
        [InlineKeyboardButton("Instagram", web_app=WebAppInfo(url="https://instagram.com/your_instagram"))],
        [InlineKeyboardButton("VK", web_app=WebAppInfo(url="https://m.vk.com/barbermanspb"))],
        [InlineKeyboardButton("Написать сообщение", url="https://t.me/BARBERMANSPB")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Используем callback_query.message для отправки фото
    await update.callback_query.message.reply_photo(
        photo="https://avatars.mds.yandex.net/get-altay/5476806/2a0000017e6a21f86297a5246460c10df452/XXXL",
        caption="⬇️ Привет! Выберите действие ⬇️",
        reply_markup=reply_markup
    )

# Регистрация обработчика команды /start
telegram_app.add_handler(CommandHandler("start", handle_start_command))
telegram_app.add_handler(CallbackQueryHandler(handle_shaving_products, pattern="shaving_products"))
telegram_app.add_handler(CallbackQueryHandler(handle_back_to_menu, pattern="back_to_menu"))

# Обработчик вебхуков
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"status": "ok"}
