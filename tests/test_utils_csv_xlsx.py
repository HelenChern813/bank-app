from unittest.mock import patch, mock_open
from src.utils_csv_xlsx import get_transactions_csv, get_transactions_xlsx


def test_get_transactions_xlsx(fragment_xlsx):
    """Проверяет работоспособность функции"""

    file_path = "../data/transactions_excel.xlsx"
    transactions = get_transactions_xlsx(file_path)
    assert transactions[0] == fragment_xlsx


def test_get_transactions_csv(fragment_csv):
    """Проверяет работоспособность функции"""

    file_path = "../data/transactions.csv"
    transactions = get_transactions_csv(file_path)
    assert transactions[1] == fragment_csv


def test_read_from_csv_error():
    m = mock_open()
    m.side_effect = FileNotFoundError
    with patch('builtins.open', m) as mocked_open:
        assert get_transactions_csv('operations.csv') == f'Ошибка в чтении файла, возможно не корректный путь: '
    mocked_open.assert_called_with('operations.csv', 'r', encoding='utf-8')


def test_read_xlsx_error():
    m = mock_open()
    m.side_effect = FileNotFoundError
    with patch('builtins.open', m):
        assert get_transactions_xlsx('operations.xlsx') == f'Ошибка в чтении файла, возможно не корректный путь: '