from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize('card_number, expected', [
    # Успешные сценарии
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305","Счет **4305"),
    # Ошибочные сценарии
    ("Visa Platinum 700079228606361","Invalid card number"),
    ("Счет 7365410843013587430","Invalid card number"),
])
def test_mask_account_card(card_number, expected):
    assert mask_account_card(card_number) == expected
