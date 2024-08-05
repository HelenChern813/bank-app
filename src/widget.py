from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Возвращает имя карты или счет с их масками"""

    bank_info_list = bank_info.split(" ")
    if bank_info_list[0] == "Счет":
        masks_account = get_mask_account(bank_info_list[-1])
        return f"{bank_info_list[0]} {masks_account}"
    else:
        masks_card = get_mask_card_number(bank_info_list[-1])
        del bank_info_list[-1]
        name_card = " ".join(bank_info_list)
        return f"{name_card} {masks_card}"


def get_data(data_info: str) -> str:
    """Взвращает дату операции"""

    if len(data_info) == 26:
        return f"{data_info[0:4]}.{data_info[5:7]}.{data_info[8:10]}"
    return "Не правильные данные"
