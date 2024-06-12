def filter_by_state(infor_operation: list, key_state: str = "EXECUTED") -> list:
    """Функция возвращающая список операций с определенным состоянием"""

    new_inf_operation = []
    for i in range(len(infor_operation)):
        if infor_operation[i]["state"] == key_state:
            new_inf_operation.append(infor_operation[i])
    return new_inf_operation


def sort_by_date(infor_operation: list, sort_: bool = True) -> list:
    """Функция возвращает отсортированные операции по дате"""

    new_inf_operation = sorted(infor_operation, key=lambda datas: datas.get("date"), reverse=sort_)
    return new_inf_operation
