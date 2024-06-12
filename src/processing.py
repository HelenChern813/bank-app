def filter_by_state(infor_operation: list, key_state="EXECUTED") -> list:
    """Функция возвращающая список операций с определенным состоянием"""

    new_inf_operation = []
    for i in range(len(infor_operation)):
        if infor_operation[i]["state"] == key_state:
            new_inf_operation.append(infor_operation[i])
    return new_inf_operation
