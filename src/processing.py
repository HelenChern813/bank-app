def filter_by_state(operation_list: list, key_state: str = "EXECUTED") -> list:
    """Функция возвращающая список операций с определенным состоянием"""

    filtered_list = []
    for i in range(len(operation_list)):
        if operation_list[i]["state"] == key_state:
            filtered_list.append(operation_list[i])
    return filtered_list


def sort_by_date(infor_operation: list, is_descending: bool = True) -> list:
    """Функция возвращает отсортированные операции по дате"""

    sorted_list = sorted(infor_operation, key=lambda operation: operation.get("date"), reverse=is_descending)
    return sorted_list
