import pytest
from src.decorators import log


def test_log():
    '''Тест работы декоратора'''
    @log()
    def my_function(x, y):
        return (x + y)

    result = my_function(6, 5)
    assert result == 11

def test_log_capsys(capsys):
    '''Тест вывода на консоль'''
    @log()
    def my_function(x, y):
        return (x + y)

    my_function(6, 5)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n\n'

def test_log_error():
    '''Тест вызова исключения'''
    with pytest.raises(Exception):
        def my_function(x, y):
            return (x + y)
        my_function(6, '5')

