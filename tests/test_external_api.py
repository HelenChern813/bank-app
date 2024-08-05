from unittest.mock import MagicMock, patch

from src.external_api import convert_exchange_rate, summ_amount


def test_summ_amount_rub(transaction_rub):
    """Тест работы функции с рублями"""

    assert summ_amount(transaction_rub) == 1.23


@patch("src.external_api.convert_exchange_rate")
def test_summ_amount_eur(convert_mock, transaction_eur):
    """Тест работы функции с другой валютой (евро)"""

    convert_mock.return_value = 100

    assert summ_amount(transaction_eur) == 123


@patch("requests.get")
def test_convert_exchange_rate(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 1.0}}
    mock_get.return_value = mock_response

    assert convert_exchange_rate("USD") == 1.0
