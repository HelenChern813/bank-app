from masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    bank_info_list = bank_info.split(" ")
    if bank_info_list[0] == "Счет":
        masks_account = get_mask_account(bank_info_list[-1])
        return f"{bank_info_list[0]} {masks_account}"
    else:
        masks_card = get_mask_card_number(bank_info_list[-1])
        del bank_info_list[-1]
        name_card = " ".join(bank_info_list)
        return f"{name_card} {masks_card}"
