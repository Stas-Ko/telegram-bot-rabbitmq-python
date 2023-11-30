#Файл test_external_api.py содержит юнит-тесты для взаимодействия с внешним API.
#Он использует библиотеку pytest для написания и запуска тестов.

import pytest
import requests_mock
from external_api import send_message_to_external_api

def test_send_message_to_external_api():
    # Мокаем запрос к внешнему API и проверяем, что сообщение успешно отправляется
    with requests_mock.Mocker() as m:
        url = '<external-api-url>'
        m.post(url, status_code=200)

        send_message_to_external_api('Hello, API')
        assert m.called_once

        request = m.request_history[0]
        assert request.url == url
        assert request.method == 'POST'
        assert request.json() == {'message': 'Hello, API'}
