import asyncio
from dotenv import load_dotenv
from bot import TelegramBot
from rabbitmq import RabbitMQConsumer
from external_api import send_message_to_external_api

load_dotenv()

async def consume_messages():
    bot = TelegramBot()
    consumer = RabbitMQConsumer()
    await consumer.connect()

    while True:
        message = await consumer.consume_message()
        if message == 'print':
            last_message = await bot.get_last_message()
            print(last_message)
        elif message == 'send':
            last_message = await bot.get_last_message()
            await send_message_to_external_api(last_message)

async def main():
    await consume_messages()

if __name__ == '__main__':
    asyncio.run(main())
