import os
import requests

async def send_message_to_external_api(message):
    external_api_url = os.getenv('EXTERNAL_API_URL')
    data = {
        'message': message
    }
    response = requests.post(external_api_url, json=data)
    if response.status_code == 200:
        print('Message sent to external API successfully')
    else:
        print('Failed to send message to external API')
