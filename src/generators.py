from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[dict, None, None]:
    """Фильтрует транзакции по типу валюты"""

    filter_transactions = list(
        filter(lambda i: i["operationAmount"]["currency"].get("code") == currency, transactions)
    )
    for i in range(len(filter_transactions)):
        yield filter_transactions[i]


def transaction_descriptions(transactions: dict) -> Generator[str, None, None]:
    """Возвращает описание операции"""

    for i in transactions:
        yield i.get("description")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номер карты с указанием интервала"""

    for i in range(start, stop + 1):
        num = (16 - len(str(i))) * "0" + str(i)
        yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:16]}"
