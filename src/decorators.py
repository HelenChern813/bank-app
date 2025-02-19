from typing import Callable, Any


def log(filename: Any = None) -> Callable:
    """Генератор логирования в заданный файл или на консоль"""

    def wrapper(function: Callable) -> Callable:
        def inner(*args: Any) -> Any:
            try:
                result = function(*args)
            except Exception as e:
                if filename == None:
                    return print(f"my_function error: {e}. Inputs: {args}\n")
                else:
                    file = open(filename, "a")
                    file.write(f"my_function error: {e}. Inputs: {args}\n")
            else:
                if filename == None:
                    print("my_function ok\n")
                    return result
                else:
                    file = open(filename, "a")
                    file.write("my_function ok\n")
                    return result

        return inner

    return wrapper


if __name__ == "__main__":

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
