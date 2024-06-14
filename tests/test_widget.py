import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "my_facts, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(my_facts, expected):
    assert mask_account_card(my_facts) == expected


def test_get_data(string_error):
    assert get_data([]) == string_error
