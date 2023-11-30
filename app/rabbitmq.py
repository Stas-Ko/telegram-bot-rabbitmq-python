import os
import aioamqp

class RabbitMQConsumer:
    async def connect(self):
        self.amqp_user = os.getenv('AMQP_USER')
        self.amqp_password = os.getenv('AMQP_PASSWORD')
        self.amqp_address = os.getenv('AMQP_ADDRESS')
        self.amqp_vhost = os.getenv('AMQP_VHOST')
        self.amqp_port = os.getenv('AMQP_PORT')

        self.protocol = await aioamqp.connect(
            host=self.amqp_address,
            port=self.amqp_port,
            login=self.amqp_user,
            password=self.amqp_password,
            virtualhost=self.amqp_vhost
        )
        self.channel = await self.protocol.channel()

        await self.channel.queue_declare(queue_name='0', durable=True)

    async def consume_message(self):
        await self.channel.basic_qos(prefetch_count=1)
        message = await self.channel.basic_get(queue_name='0')
        if message:
            await self.channel.basic_ack(delivery_tag=message.delivery_tag)
            return message.body.decode()
