from src.masks import get_mask_card_number, get_mask_account
import pytest

def tests_get_mask_card_number():
    """Тест функции которая маскирует номер карты, показывая первые 6 и последние 4 цифры."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def tests_get_mask_account():
    """Тест функции которая маскирует номер счета, показывая паследние 4 цифры."""
    assert get_mask_account("73654108430135874305") == "**4305"