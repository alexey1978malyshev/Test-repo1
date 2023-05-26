# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.#
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.
#
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
#(*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X, выводим все числа в отсортированном виде (по возрастанию)
import random

num_list = [random.randint(i, 99) for i in range(1, 11)]
print(num_list)
#num_list = [10, 5, 7, 3, 3, 2, 5, 7, 4, 3, 8]

x = int(input('Введите число: '))

closest_elem = num_list[0]
lst_of_closest = []

for i in num_list:
    if abs(i - x) < abs(closest_elem - x) and abs(i - x) != 0:
        closest_elem = i

for k in num_list:
    if abs(k - x) == abs(closest_elem - x):
        lst_of_closest.append(k)
lst_of_closest.sort()

print(closest_elem)
print(lst_of_closest)
