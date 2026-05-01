import os

import pytest
from dotenv import load_dotenv

from src.utils import load_Json
from src.utils import sum_conversion

load_dotenv()
way = os.getenv("MY_TEST")


@pytest.mark.parametrize(
    "path, expected",
    [
        (
            f"{way}test_5.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                },
            ],
        ),
        (f"{way}test_1.json", []),
        (f"{way}test_2.json", []),
        ("", []),
    ],
)
def test_load_Json(path: str, expected: list) -> None:
    """Тестирование функции открывающей файл"""
    assert load_Json(path) == expected


@pytest.mark.parametrize("path, expected", [(f"{way}test_5.json", 80180.63)])
def test_sum_conversion(path: str, expected: float) -> None:
    """Тестирование функции для подсчета суммы транзакции"""
    assert sum_conversion(path) == expected
