card_number = input("Введите номер карты: ")

account_number = input("Введите номер счета: ")


def get_mask_card_number(card_number: str) -> str:
    """Преобразует номер карты в маску карты"""

    new_substring = "*"
    card_number_list = list()
    for i in range(len(card_number)):
        card_number_list.append(card_number[i])

    for i in range(6, 12):
        del card_number_list[i]
        card_number_list.insert(i, new_substring)

    str_1 = "".join(card_number_list[0:4])
    str_2 = "".join(card_number_list[4:8])
    str_3 = "".join(card_number_list[8:12])
    str_4 = "".join(card_number_list[12:])

    final_str_card = " ".join([str_1, str_2, str_3, str_4])
    return final_str_card


def get_mask_account(account_number: str) -> str:
    """Преобразует номер счета в маску счета"""

    new_substring = "*"
    account_number_list = list()
    for i in range(len(account_number) - 6, len(account_number)):
        account_number_list.append(account_number[i])

    for i in range(0, 2):
        del account_number_list[i]
        account_number_list.insert(i, new_substring)

    final_str_account = "".join(account_number_list)

    return final_str_account
