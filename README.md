### Функционал приложения

### Технологии
FastAPI Python

### Структура приложения

client-records-telegram-bot/
│
├── api/
│   └── index.py             # Основной файл с кодом бота
├── venv/                    # Виртуальное окружение (не добавляйте в Git)
├── .gitignore               # Исключение виртуального окружения из репозитория
├── requirements.txt         # Зависимости проекта
├── vercel.json              # Конфигурация Vercel для маршрутизации
├── README.md                # Документация для проекта (опционально)
└── .env                     # Переменные окружения (не для публичного репозитория)


### Установка библиотек
python3 -m venv venv
source venv/bin/activate

pip freeze > requirements.txt
pip --version
pip install --upgrade pip

pip install python-telegram-bot==20.5
pip install fastapi
pip install python-dotenv
pip install -r requirements.txt

pip install uvicorn

### Запуск приложения с помощью uvicorn:

uvicorn index:app --reload

можно будет перейти по адресу http://127.0.0.1:8000
