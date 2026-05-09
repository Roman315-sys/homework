import csv
import logging
import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger("work_csv")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f'{os.getenv("MY_WAY")}logs/work_csv.log', mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def load_csv(path: str) -> list:
    """Чтение файла с расширением CSV"""
    try:
        if os.path.getsize(path) == 0:
            logger.warning(f"Файл {path} пустой")
            return []
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=';')
            return list(reader)
    except FileNotFoundError:
        logger.warning(f"Файл {path} не найден")
        return []


def load_excel(path: str) -> list:
    """Чтение файла с расширением XLSX"""
    try:
        df = pd.read_excel(path)
        result = df.to_dict('records')
        if len(result) > 0:
            return result
        else:
            return []
    except FileNotFoundError:
        logger.warning(f"Файл {path} не найден")
        return []
