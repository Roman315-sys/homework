from src.masks import get_mask_card_number, get_mask_account
import pytest

@pytest.mark.parametrize('card_number, expected', [
    # Успешные сценарии
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    # Ошибочные сценарии
    ("000792289606361", "Invalid card number"),
    ("70007922896063611", "Invalid card number"),
    ("abcd123456789012", "Invalid card number"),
    ("", "Invalid card number")
])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('score_number, exp',[
    # Успешные сценарии
    ('73654108430135874305', "**4305"),
    ('12345678901234561233', "**1233"),
    ('00000000000000000000', "**0000"),
    ('11112222333344444444', "**4444"),
    # Ошибочные сценарии
    ('12345', "Invalid card number"),
    ('123456789012345678901', "Invalid card number"),
    ('abcd123456789012', "Invalid card number"),
    ("", "Invalid card number"),
    ("qwertyuiopasdfghjklz", "Invalid card number")
])
def tests_get_mask_account(score_number: str, exp:str) -> None:
    """Тест функции которая маскирует номер счета, показывая паследние 4 цифры."""
    assert get_mask_account(score_number) == exp


def tests_get_mask_card_number(masks_1: str) -> None:
    assert get_mask_card_number("7000792289606361") == masks_1


def test_get_mask_account(masks_2:str) -> None:
    """Тест функции которая маскирует номер счета, показывая паследние 4 цифры."""
    assert get_mask_account('73654108430135874305') == masks_2

