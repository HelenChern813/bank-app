import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(str_number_card):
    """Проверяет работоспособность функции"""

    assert get_mask_card_number("7000792289606361") == str_number_card


def test_mask_card_error():
    """Ожидаемая ошибка TypeError"""

    with pytest.raises(TypeError):
        get_mask_card_number(7000792289606361)


@pytest.mark.parametrize("my_facts, expected", [("73654108430135874305", "**4305"), ("7000792289606361", "**6361")])
def test_mask_account(my_facts, expected):
    """Проверяет работоспособность функции"""

    assert get_mask_account(my_facts) == expected


def test_mask_account_error():
    """Ожидаемая ошибка TypeError"""

    with pytest.raises(TypeError):
        get_mask_account(123)
