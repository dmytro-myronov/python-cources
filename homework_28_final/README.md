# 🚗 Carsharing Platform

A full-featured car rental service built with Django and Django REST Framework.  
Includes an anonymous-friendly Telegram chatbot, asynchronous background tasks, Dockerized deployment, and developer tools for convenience.

## 📦 Features

- User registration and authentication
- Car management via REST API
- Car rental order creation (for registered users and anonymous guests)
- Telegram bot integration for quick, anonymous order placement
- Celery with Celery Beat for background tasks
- Dockerized for easy deployment
- Aliases and Makefile for convenient development commands
- Environment configuration via `.env`

## 🧰 Technologies

- Python, Django, Django REST Framework
- PostgreSQL
- Celery & Celery Beat
- Docker & Docker Compose
- Telegram Bot (python-telegram-bot)
- httpx (for async bot HTTP requests)

## 🤖 Telegram Bot

The Telegram bot allows anonymous users to:

- View a list of available cars
- Select a car and provide name/email
- Create an order without requiring a registered user account

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:dmytro-myronov/python-cources.git
cd https://github.com/dmytro-myronov/python-cources/tree/main/homework_28_final
docker-compose up -d --build
or make up
```

### 2. Configure Environment

Create a `.env` file based on `.env.example` and configure your settings.

### 3. Run the project

```bash
make up            #  Builds Docker containers and Starts all services
make run       # run server
make shell   # Connect to container

```

### 4. Start Celery Worker & Beat (optional)

```bash
make worker        # Starts Celery worker
make beat          # Starts Celery Beat for periodic tasks
```

## 🧪 Running Tests

```bash
make test
```

## 🧾 License

MIT License.  
Feel free to fork, extend, and contribute.
