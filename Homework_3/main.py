from typing import List
from functools import reduce


def even_numbers(numbers_list: List[int]) -> None:
    even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers_list))
    if even_numbers_list:
        print(f"Четные числа: {even_numbers_list}")
        sum_average_value_numbers(even_numbers_list)
    else:
        print("Четные числа отсутствуют")


def sum_average_value_numbers(numbers_list) -> None:
    sum_numbers = reduce(lambda x, y: x + y, numbers_list)
    average_value_numbers = sum_numbers / len(numbers_list)
    print(f"Сумма четных чисел: {sum_numbers}")
    print(f"Среднее значение четных чисел: {average_value_numbers:.1f}")


numbers = list(map(int, (input("Введите числа через пробел: ").split())))
even_numbers(numbers)
