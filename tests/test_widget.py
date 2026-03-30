from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize('card_number, expected', [
    # Успешные сценарии
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305","Счет **4305"),
    # Ошибочные сценарии
    ("Visa Platinum 700079228606361","Invalid card number"),
    ("Счет 7365410843013587430","Invalid card number"),
    ("Visa Platinum","Invalid card number"),
    ("7365410843013587430","Invalid card number")
])
def test_mask_account_card(card_number: str, expected:str) -> None:
    assert mask_account_card(card_number) == expected


@pytest.mark.parametrize('date, expected', [
    # Успешные сценарии
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    # Ошибочные сценарии
    ("2024-03-11T02:26:18.6", "Incorrect date format"),
    ("202e-03-11T02:26:18.671407", "Incorrect date format"),
    ("2024-0r-11T02:26:18.671407", "Incorrect date format"),
    ("2024-03-1sT02:26:18.671407", "Incorrect date format"),
    ("2024--11T02:26:18.671407", "Incorrect date format")
])
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected


def tests_mask_account_card(widget_1:str) -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == widget_1


def tests_get_date(widget_2:str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == widget_2


