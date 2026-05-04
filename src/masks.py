import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/user/PycharmProjects/homework/logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(argument: str) -> str:
    """Маскирует номер карты, показывая первые 6 и последние 4 цифры."""
    logger.info(f"Маскировка номера карты: {argument}")
    # Проверка коректности ввода!
    if len(argument) != 16:
        logger.warning(f"Некорректная длина номера карты: {len(argument)} (ожидается 16)")
        return "Invalid card number"
    if not argument.isdigit():
        logger.warning(f"Номер карты содержит нецифровые символы: {argument}")
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
    logger.info(f"Номер карты {argument} успешно замаскирован!")
    return f"{final[:4]} {final[4:8]} {final[8:12]} {final[12:16]}"


def get_mask_account(argument: str) -> str:
    """Маскирует номер счета, показывая паследние 4 цифры."""
    logger.info(f"Маскировка номера счёта: {argument}")
    # Проверка коректности ввода!
    if len(argument) != 20:
        logger.warning(f"Некорректная длина номера счёта: {len(argument)} (ожидается 20)")
        return "Invalid card number"
    if not argument.isdigit():
        logger.warning(f"Номер счёта содержит нецифровые символы: {argument}")
        return "Invalid card number"
    # Реализация функци!
    last_digits = argument[-4:]
    stars = "*" * 2
    logger.info(f"Номер счёта {argument} успешно замаскирован")
    return stars + last_digits
