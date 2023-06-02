# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3

def sum_two_num(a: int, b: int) -> int:
    if a >= 0:
        return b if a == 0 else sum_two_num(a - 1, b) + 1
    raise 'Argument "a" must have a positive value'


print(sum_two_num(0, 23))
