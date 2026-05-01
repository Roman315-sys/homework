import os
from unittest.mock import patch

from src.external_api import currency_conversion

d = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
}


@patch("requests.get")
def test_currency_conversion(mock_get):
    """Тестирование API запроса"""
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 25, "from": "GBP", "to": "JPY"},
        "result": 3724.305775,
        "success": True,
    }
    assert currency_conversion(d) == 3724.305775
    mock_get.assert_called_once_with(
        os.getenv("MY_URL"),
        params={"amount": "8221.37", "from": "USD", "to": "RUB"},
        headers={"apikey": os.getenv("API_KEY")},
    )
