# telegram-bot-rabbitmq-python

## Описание

Этот проект представляет собой сервис для создания Telegram-бота, интегрированного с RabbitMQ и взаимодействующего с внешним API.

Основная цель проекта - предоставить инструмент для создания Telegram-ботов с расширенными возможностями, такими как интеграция с очередью сообщений RabbitMQ и взаимодействие с внешними API.

Функциональность проекта включает:

Прием и обработку сообщений от пользователей через Telegram Bot API. Бот может получать текстовые сообщения, изображения, аудио, видео и другие мультимедийные данные от пользователей.
Отправку сообщений внешнему API для выполнения определенных действий. Например, бот может отправлять запросы к внешнему API для получения информации, выполнения расчетов или выполнения других задач.
Интеграцию с RabbitMQ для обмена сообщениями с другими сервисами. Бот может отправлять и получать сообщения через RabbitMQ, что позволяет ему взаимодействовать с другими компонентами системы в асинхронном режиме.
Проект имеет гибкую и расширяемую архитектуру, что позволяет легко добавлять новую функциональность и настраивать его под конкретные требования проекта.

Он включает следующие компоненты:

main.py: Основной файл приложения, который запускает Telegram-бота и обрабатывает входящие сообщения.
bot.py: Модуль, содержащий класс TelegramBot, который обрабатывает входящие сообщения от пользователей и отправляет ответы.
rabbitmq.py: Модуль, содержащий класс RabbitMQConsumer, который отвечает за прием и обработку сообщений из RabbitMQ.
external_api.py: Модуль, содержащий функцию send_message_to_external_api, которая отправляет сообщения во внешнее API.
tests/: Папка с модульными тестами для основных компонентов проекта.
Проект также включает файлы Dockerfile и docker-compose.yml, которые облегчают развертывание и запуск проекта в контейнерах Docker.

В этом README файле вы найдете инструкции по установке, запуску и тестированию проекта, а также информацию о вкладе в проект и лицензии.

## Зависимости

Для работы этого проекта необходимо установить следующие зависимости:

- Python 3.7 или выше
- python-telegram-bot (v13.7 или выше)
- pika (v1.2.0 или выше) для взаимодействия с RabbitMQ
- requests (v2.26.0 или выше)
- Docker (по желанию для развертывания в контейнерах)
- Docker Compose (по желанию для управления многоконтейнерными приложениями)

Вы можете установить эти зависимости с помощью pip, выполнив следующую команду:

Не забудьте также добавить файл `requirements.txt`, содержащий список зависимостей и их версий.


## Функциональность

- Прием и обработка сообщений от пользователей через Telegram Bot API.
- Отправка сообщений внешнему API для выполнения определенных действий.
- Интеграция с RabbitMQ для обмена сообщениями с другими сервисами.

## Структура проекта

- `app/main.py`: Основной файл приложения, запускающий Telegram-бота.
- `app/bot.py`: Модуль, содержащий класс `TelegramBot` для обработки сообщений от пользователей.
- `app/rabbitmq.py`: Модуль, содержащий класс `RabbitMQConsumer` для приема и обработки сообщений из RabbitMQ.
- `app/external_api.py`: Модуль, содержащий функцию `send_message_to_external_api` для отправки сообщений во внешнее API.
- `app/tests/`: Папка с модульными тестами для основных компонентов проекта.
- `Dockerfile`: Файл для создания Docker-образа проекта.
- `docker-compose.yml`: Файл для запуска проекта в контейнерах Docker.
- `README.md`: Файл, который вы сейчас читаете. Он содержит описание проекта и инструкции по его запуску.

## Установка и запуск

1. Убедитесь, что у вас установлен Python версии 3.x и Docker.

2. Клонируйте репозиторий проекта:
git clone https://github.com/Stas-Ko/telegram-bot-rabbitmq-python.git

3. Перейдите в директорию проекта:
cd telegram-bot-service

4. Запустите проект с помощью Docker Compose:
docker-compose up

Проект будет запущен в контейнерах Docker, и Telegram-бот будет доступен для взаимодействия.

## Тестирование

1. Убедитесь, что проект запущен с помощью Docker Compose.

2. Перейдите в директорию проекта:

cd telegram-bot-service

3. Запустите тесты с помощью Pytest:

pytest app/tests

Pytest выполнит модульные тесты для основных компонентов проекта и выведет результаты в терминале.







