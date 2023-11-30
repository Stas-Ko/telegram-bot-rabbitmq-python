import pytest
from bot import TelegramBot

@pytest.fixture
def telegram_bot():
    return TelegramBot()

def test_get_last_message(telegram_bot):
    # Мокаем запрос к API Telegram и проверяем, что возвращается последнее сообщение
    # Пример использования pytest-mock
    with requests_mock.Mocker() as m:
        url = 'https://api.telegram.org/bot<api-token>/getUpdates'
        response_data = {
            'result': [
                {
                    'message': {
                        'text': 'Hello, World!'
                    }
                }
            ]
        }
        m.get(url, json=response_data)
        
        last_message = telegram_bot.get_last_message()
        assert last_message == 'Hello, World!'
