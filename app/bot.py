import os
import requests

class TelegramBot:
    def __init__(self):
        self.api_token = os.getenv('TELEGRAM_API_TOKEN')

    async def get_last_message(self):
        url = f'https://api.telegram.org/bot{self.api_token}/getUpdates'
        response = requests.get(url)
        data = response.json()
        last_update = data['result'][-1]
        last_message = last_update['message']['text']
        return last_message
