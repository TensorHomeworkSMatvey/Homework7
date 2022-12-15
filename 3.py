def fib(n):
    """Вернёт n-ое число Фибоначи"""
    assert type(n) == int, "Введен неправильный тип-данных"
    assert n >= 1, "Число меньше 1 или не соответствует типу"
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print("Число Фибоначи:", fib(6))