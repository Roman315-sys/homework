def get_mask_card_number(argument: str) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры."""
    result   = []
    for i, char in enumerate(argument):
        if i < 6:
            result.append(char)
        elif i >= len(argument) - 4:
            result.append(char)
        else:
            result.append("*")
    final = "".join(result)
    block1 = final[0:4]
    block2 = final[4:8]
    block3 = final[8:12]
    block4 = final[12:16]
    return f"{block1} {block2} {block3} {block4}"


def get_mask_account(argument: str) -> str:
    result = argument[-4:]
    return f'**{result}'

