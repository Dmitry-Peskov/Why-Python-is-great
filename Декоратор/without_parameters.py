from datetime import datetime
from functools import wraps


# track_execution декоратор, который формирует сообщение с информацией о вызове и
# результате работы функции которую "украшает". Выводит сформированное сообщение в терминал
def track_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        msg = f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')} вызов {func.__name__}()" \
              f" с args {args} и kwargs {kwargs} дал результат {original_result}"
        print(msg)
        return original_result
    return wrapper


# test_func произвольная функция, которую мы украшаем нашим декоратором
@track_execution
def test_func(a: int | float, b: int | float, c: int | float) -> int | float:
    return (4*a + b**2) - c * 0.5


if __name__ == "__main__":
    # делаем несколько вызовов нашей функции, что бы посмотреть как отрабатывает декоратор
    # передаем значения и как позиционные аргументы и как именнованные
    result1 = test_func(a=10, b=4, c=15)
    result2 = test_func(3, 7, 11)
    result3 = test_func(3, 6, c=12)
    # получаем в терминал что-то вроде:
    # 27.04.2024 21:27:56 вызов test_func() с args () и kawargs {'a': 10, 'b': 4, 'c': 15} дал результат 48.5
    # 27.04.2024 21:27:56 вызов test_func() с args (3, 7, 11) и kawargs {} дал результат 55.5
    # 27.04.2024 21:27:56 вызов test_func() с args (3, 6) и kawargs {'c': 12} дал результат 42.0
