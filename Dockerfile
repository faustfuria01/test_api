FROM python:3.9-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY . .

# Переменные окружения для Flask
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Запуск приложения
CMD ["flask", "run", "--host=0.0.0.0"]