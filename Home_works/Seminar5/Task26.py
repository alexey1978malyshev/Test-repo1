# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать
# только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def pow_rec(a: int, b: int) -> int:
    return 1 if b == 0 else pow_rec(a, b - 1) * a


print(pow_rec(2, 0))
