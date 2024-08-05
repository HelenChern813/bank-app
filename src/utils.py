import json
import logging
import os
from typing import Dict, List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/src.utils.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_transactions(path: str) -> List[Dict]:
    """Возвращает список словарей, содержащих данные об транзакциях"""

    if not os.path.exists(path):
        logger.error("Файл пустой")
        return []

    try:
        logger.info("Получаем данные о транзакциях в формате JSON")
        with open(path, "r", encoding="utf-8") as file:
            transaction = json.load(file)

    except json.JSONDecodeError as er:
        logger.error(f"Произошла ошибка в файле формата JSON: {er}")
        return []

    if not isinstance(transaction, list):
        logger.error("Некорректный тип данных в файле формата JSON")
        return []

    return transaction
