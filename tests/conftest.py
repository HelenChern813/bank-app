import pytest


@pytest.fixture()
def str_number_card():
    return "7000 79** **** 6361"


@pytest.fixture()
def string_error():
    return "Не правильные данные"
