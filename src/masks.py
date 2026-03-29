def get_mask_card_number(argument: str) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры."""
    # Проверка коректности ввода!
    if len(argument) != 16:
        return "Invalid card number"
    if not argument.isdigit():
        return "Invalid card number"
    # Реализация функци!
    result = []
    for i, char in enumerate(argument):
        if i < 6:
            result.append(char)
        elif i >= len(argument) - 4:
            result.append(char)
        else:
            result.append("*")
    final = "".join(result)
    return f"{final[:4]} {final[4:8]} {final[8:12]} {final[12:16]}"


def get_mask_account(argument: str) -> str:
    """Маскирует номер счета, показывая паследние 4 цифры."""
    # Проверка коректности ввода!
    if len(argument) != 20:
        return "Invalid card number"
    if not argument.isdigit():
        return "Invalid card number"
    # Реализация функци!
    last_digits = argument[-4:]
    stars = "*" * 2
    return stars + last_digits
