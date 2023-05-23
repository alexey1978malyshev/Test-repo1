# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.#
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

import math

summa = int(input('Введите сумму: '))
multiple = int(input('Введите произведение: '))

result_1 = 0
result_2 = 0

# for i in range(summa):
#     for j in range(summa):
#         if i * j == multiple and i + j == summa:
#             result_1 = i
#             result_2 = j
#             break


# ну или математически), сложность будет константная, вроде бы, или даже единичная... вместо квадратичной
# summa = result_1 + result_2
# multiple = result_1 * result_2
# result_1 = summa - result_2
# result_1 = multiple / result_2 ==>
# ==> summa - result_2 = multiple / result_2 ==>
# ==> multiple = result_2 * (summa - result_2) ==>
# ==> -result_2 **2 + result_2 * summa - multiple = 0  сводим всё безобразие к квадратному уравнению

d = math.pow(summa, 2) - 4 * -1 * -multiple  # находим дискриминант
result_2 = (-summa + math.sqrt(d)) / 2 * -1  # и корень... хватит одного
result_1 = summa - result_2

print(f'{result_1} **** {result_2}')
