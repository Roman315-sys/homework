import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(i: dict) -> float:
    """Функция для перевода любой валюты в рубли"""
    url = os.getenv("MY_URL")
    api_key = {"apikey": os.getenv("API_KEY")}
    params = {"amount": i["operationAmount"]["amount"], "from": i["operationAmount"]["currency"]["code"], "to": "RUB"}
    response = requests.get(url, headers=api_key, params=params)
    return response.json()["result"]
