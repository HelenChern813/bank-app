import re
from collections import Counter

from src.utils import get_transactions


def filter_by_state(operation_list: list, key_state: str = "EXECUTED") -> list:
    """Функция возвращающая список операций с определенным состоянием"""

    filtered_list = []
    for i in operation_list:
        if i["state"] == key_state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(infor_operation: list, is_descending: bool = True) -> list:
    """Функция возвращает отсортированные операции по дате"""

    sorted_list = sorted(infor_operation, key=lambda operation: operation.get("date"), reverse=is_descending)
    return sorted_list


def search_by_description(operations: list[dict], user_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска
    и возвращает список словарей, у которых в описании есть данная строка
    """

    return [operation for operation in operations if re.search(user_search.lower(), operation["description"].lower())]


def get_count_operations_by_category(operations: list[dict], list_of_category: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    result = Counter(
        [operation["description"] for operation in operations if operation["description"] in list_of_category]
    )

    return dict(result)


if __name__ == "__main__":
    file = get_transactions("../data/operations.json")
    print(file)
    print(filter_by_state(file))
