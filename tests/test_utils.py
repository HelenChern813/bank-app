from unittest.mock import mock_open, patch

from src.utils import get_transactions


@patch("os.path.exists")
def test_get_transactions(mock_os_path_exists):
    """Проверяет, что если файл не существует, возвращается пустой список."""

    mock_os_path_exists.return_value = False  # задаём фальшивому .exists что он возвращает False
    assert get_transactions("operations.json") == []


def test_get_transactions_file_not_json():

    mock_open(read_data="not_json_data")
    assert get_transactions("operations.json") == []


@patch("os.path.exists")
def test_get_transactions_invalid_json(mock_os_path_exists):

    mock_os_path_exists.return_value = True
    m = mock_open(read_data='{"amount": "200", "currency": "USD"}')
    with patch("builtins.open", m) as mocked_open:
        assert (
            get_transactions("operations.json") == []
        )  # если в файле не список, функция должна вернуть пустой список
        mocked_open.assert_called_with("operations.json", "r", encoding="utf-8")
