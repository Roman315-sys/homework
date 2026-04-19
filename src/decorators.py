from functools import wraps
from time import time
from typing import Optional


def log(filename: Optional[str] = None):
    """Декораторр для обработки информации о функции"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                beginning = time()
                result = func(*args, **kwargs)
                end = time()
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n " f"function result {result}\n")
                else:
                    print(
                        f"{func.__name__} ok\n"
                        f"function result: {result}\n"
                        f"function operation time {end - beginning}"
                    )
            except Exception as e:
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. inputs: {args}, {kwargs}")
                raise

        return wrapper

    return my_decorator
