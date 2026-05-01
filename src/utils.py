import json
import os

from src.external_api import currency_conversion


def load_Json(path: str) -> list:
    """Функция для читения файла с транзакциями"""
    try:
        if os.path.getsize(path) == 0:
            return []
        with open(path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def sum_conversion(path: str) -> float:
    """Функция для получения информации о суммах транзакции (в рублях)"""
    data = load_Json(path)

    total = 0

    for item in data:
        if item["operationAmount"]["currency"]["code"] == "RUB":
            total += float(item["operationAmount"]["amount"])
        elif item["operationAmount"]["currency"]["code"] != "RUB":
            total += currency_conversion(item)
    return total
