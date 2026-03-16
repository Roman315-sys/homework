"""Модуль для маскировки данных банковских карт и счетов."""

from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Принимает строку с типом и номером карты/счета, разделенные пробелом.
    Возвращает строку с замаскированным номером.
    """
    new_data = data.split()
    if len(new_data) != 2:
        result = get_mask_card_number(new_data[-1])
    if len(new_data) == 2:
        if new_data[0] == 'Счет':
            result = get_mask_account(new_data[-1])
        else:
            result = get_mask_card_number(new_data[-1])
    return result


def get_date(date_string: str) -> str:
    """
    Преобразует дату в формат "ДД.ММ.ГГГГ".
    """
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"
