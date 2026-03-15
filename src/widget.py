from masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    new_data = list(data.split())
    if len(new_data) != 2:
        result = get_mask_card_number(new_data[-1])
    if len(new_data) == 2:
        if new_data[0] == 'Счет':
            result = get_mask_account(new_data[-1])
        else:
            result = get_mask_card_number(new_data[-1])
    return result



print(mask_account_card('Visa Platinum 7000792289606361'))
print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 64686473678894779582'))
