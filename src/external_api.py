from dotenv import load_dotenv
import requests
import os

load_dotenv()

def currency_conversion(i: dict) -> float:
    url_1 = os.getenv("MY_URL")
    api_key = {"apikey":  os.getenv("API_KEY")}
    amount = i["operationAmount"]["amount"]
    f = i["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f'{url_1}to={to}&from={f}&amount={amount}'
    response = requests.get(url, headers=api_key)
    return response.json()["result"]