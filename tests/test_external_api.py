from unittest.mock import patch

from src.external_api import summ_amount


@patch("amount_float")
def test_summ_amount_rub(mock_sum):
    """Тест работы функции"""

    transaction_rub = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    mock_sum.return_value = 319571.58
    assert summ_amount(transaction_rub) == 319571.58


@patch("exchange_rate")
def test_summ_amount(mock_exchange_rate):
    """Тест работы функции"""

    transaction_currency = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_exchange_rate.return_value = 1
    assert summ_amount(transaction_currency) == 8221.37
