from functools import wraps


# repeat декоратор, который позволяет организовать вызов одной и той же функции quantity раз подряд
def repeat(quantity: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(quantity):
                func(*args, **kwargs)
        return wrapper
    return decorator


# test_func произвольная функция, которую мы украшаем нашим декоратором
@repeat(quantity=3)
def test_func(name: str) -> None:
    print(f"Привет {name}")


if __name__ == "__main__":
    # вызываем украшенную декоратором тестовую функции
    test_func("Иван")
    # получаем в терминал:
    # Привет Иван
    # Привет Иван
    # Привет Иван
