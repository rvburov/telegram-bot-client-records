# Client Records Telegram Bot

Бот для записи клиентов и предоставления информации о продуктах и услугах.

---

## 📋 Функционал приложения

- Отправка сообщений с фото, кнопками и ссылками.
- Интерактивное меню с переходами между разделами.
- Возможность записи через веб-приложение YClients.
- Просмотр продукции для бритья с возможностью вернуться в главное меню.
- Быстрый доступ к отзывам, Instagram, VK и маршруту до барбершопа.

---

## 🛠️ Технологии

- **Python**
- **FastAPI**
- **Python Telegram Bot** (версия 20.5)
- **Vercel** (для маршрутизации)
- **Uvicorn** (для запуска FastAPI)

---

## 📂 Структура приложения

```bash
client-records-telegram-bot/
│
├── api/
│   └── index.py             # Основной файл с кодом бота
├── venv/                    # Виртуальное окружение (не добавляйте в Git)
├── .gitignore               # Исключение виртуального окружения из репозитория
├── requirements.txt         # Зависимости проекта
├── vercel.json              # Конфигурация Vercel для маршрутизации
├── README.md                # Документация для проекта
└── .env                     # Переменные окружения (не для публичного репозитория)
```

---

## 🚀 Установка и настройка телеграм-бота

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/client-records-telegram-bot.git
cd client-records-telegram-bot
```

### 2. Установите Homebrew (Linux/MacOS)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew --version
```

#### Apple Silicon (M1/M2):

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"
```

#### Intel:

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/usr/local/bin/brew shellenv)"
```

### 3. Установите Python

```bash
brew install python
python3 --version
```

### 4. Настройте виртуальное окружение и зависимости

```bash
python3 -m venv venv             # Создаем виртуальное окружение в папке `venv`
source venv/bin/activate         # Активируем виртуальное окружение (Linux/MacOS)
venv\Scripts\activate            # Активируем виртуальное окружение (Windows)
```

```bash
pip install --upgrade pip        # Обновляем `pip` до последней версии
pip install -r requirements.txt  # Устанавливаем зависимости из `requirements.txt`
```

📦 **Установка библиотек:**

```bash
pip install python-telegram-bot==20.5
pip install fastapi python-dotenv uvicorn
pip freeze > requirements.txt    # Сохраняем зависимости
```

---

## 🌐 Настройка и запуск Webhooks на локальном сервере

Для подключения Webhooks понадобится публичный HTTPS-адрес. Используем **ngrok** для создания безопасных туннелей:

```bash
brew install --cask ngrok        # Устанавливаем ngrok
ngrok config add-authtoken <YOUR_AUTH_TOKEN>  # Добавляем токен
```

1. Запустите локальный сервер FastAPI:

    ```bash
    uvicorn api.index:app --reload
    ```

2. Запустите ngrok и получите HTTPS-адрес:

    ```bash
    ngrok http 8000
    ```

3. Настройте Webhook для Telegram:

    ```bash
    curl -X POST "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook" -d "url=https://<NGROK_URL>/webhook"
    ```

Проверьте статус Webhook:

```bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/getWebhookInfo"
```

---

## 🚀 Настройка и деплой на Vercel

### 1. Установите Node.js и Vercel CLI

```bash
brew install node
npm install -g vercel
```

### 2. Авторизуйтесь в Vercel

```bash
vercel login
```

### 3. Создайте файл `vercel.json`

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/api/index" }]
}
```

### 4. Деплой проекта

```bash
vercel  # Первый деплой
vercel --prod  # Повторный деплой
```

Добавьте переменные окружения в Vercel:

```bash
vercel env add BOT_TOKEN
vercel env add APP_URL
```

Настройте Webhook для Vercel:

```bash
curl -X POST "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook" -d "url=https://<VERCEL_URL>/webhook"
```

Проверьте статус:

```bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/getWebhookInfo"
```
