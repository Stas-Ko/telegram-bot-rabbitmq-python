import pytest
from rabbitmq import RabbitMQConsumer

@pytest.fixture
async def rabbitmq_consumer():
    consumer = RabbitMQConsumer()
    await consumer.connect()
    return consumer

@pytest.mark.asyncio
async def test_consume_message(rabbitmq_consumer):
    # Создаем тестовую очередь и отправляем в нее сообщение
    # Проверяем, что получаем правильное сообщение при его обработке
    channel = await rabbitmq_consumer.protocol.channel()
    await channel.queue_declare(queue_name='test_queue', durable=True)
    await channel.basic_publish(payload=b'test message', exchange_name='', routing_key='test_queue')

    message = await rabbitmq_consumer.consume_message()
    assert message == 'test message'
