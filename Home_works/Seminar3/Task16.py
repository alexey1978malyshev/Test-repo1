# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.#
# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2#
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1

num_list = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]

x = int(input('Введите число: '))
# count = 0
# for i in num_list:
#     if i == x:
#         count += 1
# print(count) if count != 0 else print(-1)

print(num_list.count(x)) if num_list.count(x) != 0 else print(-1)
