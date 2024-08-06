import csv
from typing import List

import pandas as pd


def get_transactions_csv(path: str) -> List[str] | str:
    """Возвращает список словарей, содержащих данные об транзакциях из CSV файла"""

    list_transactions = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            read_csv = csv.DictReader(file, delimiter=";")
            for item in read_csv:
                list_transactions.append(item)

            return list_transactions

    except FileNotFoundError as er:
        return f"Ошибка в чтении файла, возможно не корректный путь: {er}"


def get_transactions_xlsx(path: str) -> list[dict] | str:
    """Возвращает список словарей, содержащих данные об транзакциях из XLSX файла"""
    try:
        with open(path, "rb") as file:
            read_xlsx = pd.read_excel(file)
            read_xlsx_to_dict = read_xlsx.to_dict(orient="records")

            return read_xlsx_to_dict
    except FileNotFoundError as er:
        return f"Ошибка в чтении файла, возможно не корректный путь: {er}"

file_path = '.data/transactions.csv'
print(get_transactions_xlsx(file_path))