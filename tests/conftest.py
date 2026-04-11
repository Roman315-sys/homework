import pytest
from typing import List, Dict, Generator
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def masks_1() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def masks_2() -> str:
    return "**4305"


@pytest.fixture
def widget_1() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def widget_2() -> str:
    return "11.03.2024"


@pytest.fixture
def processing_1() -> list:
    return [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def processing_2() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def generators_1() -> list[dict]:
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]


@pytest.fixture
def generators_2() -> list[str]:
    return ["Перевод организации", "Перевод со счета на счет"]


@pytest.fixture
def generators_3() -> list[str]:
    return ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]