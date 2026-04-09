from typing import List, Dict, Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Generator[Dict, None, None]:
    """Сортирует список словарей по валюте"""
    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Принимает список словарей и возвращает историю переводов"""
    for i in transactions:
        yield i.get("description",  "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номера карт в заданном диапазоне"""
    for i in range(start, end + 1):
        yield f"{i:016d}"
