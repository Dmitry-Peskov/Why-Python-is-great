from typing import Optional
from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """
    Базовый абстрактный класс валидатора, с реализованной функциональностью дескриптора (методы получения и измененния значения).
    Для реализации собственного валидатора, достаточно унаследоваться от данного класса и реализовать
    метод validate.
    """
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        raise NotImplemented("Не реализован метод validate")


class NumberValidator(BaseValidator):
    """
    Конкретная реализация валидатора чисел. Позволяет при инициализации установить минимальное и максимальное значение.
    """
    def __init__(
            self,
            minvalue: Optional[int | float] = None,
            maxvalue: Optional[int | float] = None
    ):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Ожидаемый тип для {value!r} int или float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Ожидалось что {value!r} будет больше или равно {self.minvalue!r}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Ожидалось что {value!r} будет меньше или равно {self.maxvalue!r}')


if __name__ == "__main__":
    # Реализуем два класса, которые в своих конструкторах будут использовать наш NumberValidator для проверки передаваемых
    # в него значений. Для каждого класса мы можем гибко настроить минимальное и максимальное значение.
    # Если передаваемое в конструктор значение будет выходить за установленные ограничение, будет выброшено исключение.
    class User:
        uid = NumberValidator(minvalue=0, maxvalue=100)

        def __init__(self, uid: int):
            self.uid = uid

    class Order:
        number = NumberValidator(minvalue=10_00, maxvalue=1_000_000)

        def __init__(self, number: int):
            self.number = number

    user1 = User(uid=5)  # пользователь будет создан
    order1 = Order(number=20_000)  # заказ будет создан
    user2 = User(uid=-5)  # будет выброшено исключение т.к. -5 меньше 0, пользователь не будет создан
    order2 = Order(number="10")  # будет выброшено исключение т.к. "10" типа str, а ожидается int или float, заказ не будет создан
