"""Модуль для маскировки данных банковских карт и счетов."""

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    new_data = data.split()
    if new_data[0] == "Счет":
        result = get_mask_account(new_data[-1])
        if get_mask_account(new_data[-1]) == "Invalid card number":
            return "Invalid card number"
        return f'{new_data[0]} {result}'
    else:
        result = get_mask_card_number(new_data[-1])
        if get_mask_card_number(new_data[-1]) == "Invalid card number":
            return "Invalid card number"
        return f'{" ".join(new_data[:-1])} {result}'


def get_date(date_string: str) -> str:
    """Преобразует дату в формат "ДД.ММ.ГГГГ"."""
    # Проверка коректности ввода!
    if len(date_string) != 26:
        return "Incorrect date format"
    if not date_string[8:10].isdigit():
        return "Incorrect date format"
    if not date_string[5:7].isdigit():
        return "Incorrect date format"
    if not date_string[:4].isdigit():
        return "Incorrect date format"
    # Реализация функци!
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"