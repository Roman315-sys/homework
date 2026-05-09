import json
import logging
import os

from dotenv import load_dotenv

from src.external_api import currency_conversion

load_dotenv()

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f'{os.getenv("MY_WAY")}logs/utils.log', mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def load_Json(path: str) -> list:
    """Функция для читения файла с транзакциями"""
    logger.info(f"Попытка прочитать файл: {path}")
    try:
        if os.path.getsize(path) == 0:
            logger.warning(f"Файл {path} пустой")
            return []
        with open(path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                logger.info(f"Файл {path} успешно загружен, {len(data)} транзакций")
                return data
            else:
                logger.warning(f"Файл {path} содержит не список!")
                return []
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        logger.error(f"Файл {path} не найден")
        return []


def sum_conversion(path: str) -> float:
    """Функция для получения информации о суммах транзакции (в рублях)"""
    logger.info(f"Начало подсчёта суммы транзакций из файла {path}")
    data = load_Json(path)

    total = 0

    logger.info(f"Суммируем финансы из файла {path}")
    for item in data:
        if item["operationAmount"]["currency"]["code"] == "RUB":
            total += float(item["operationAmount"]["amount"])
        elif item["operationAmount"]["currency"]["code"] != "RUB":
            total += currency_conversion(item)
    logger.info("Подсчёт завершён.")
    return total
