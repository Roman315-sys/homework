"""Модуль для маскировки данных банковских карт и счетов."""

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    new_data = data.split()
    if new_data[0] == "Счет":
        result = get_mask_account(new_data[-1])
        return f'{new_data[0]}: {result}'
    else:
        result = get_mask_card_number(new_data[-1])
        return f'{" ".join(new_data[:-1])}: {result}'


def get_date(date_string: str) -> str:
    """Преобразует дату в формат "ДД.ММ.ГГГГ"."""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"