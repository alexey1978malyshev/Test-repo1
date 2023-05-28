# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только
# русские буквы и заранее известно какой алфавит надо использовать.
#
# Примеры/Тесты:
# Input:   ноутбук
# Output:  12
#
# Input:   notebook
# Output:  14
#
# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять в какую группу
# попадает буква, а также просто накапливать сумму очков.

one_point_string = "AEIOULNSTRАВЕИНОРСТ"
two_point_string = "DGДКЛМПУ"
three_point_string = "BCMPБГЁЬЯ"
four_point_string = "FHVWYЙЫ"
five_point_string = "KЖЗХЦЧ"
eigth_point_string = "JXШЭЮ"
ten_point_string = "QZФЩЪ"

input_word = input()
dict_point_count = {one_point_string: 1, two_point_string: 2, three_point_string: 3, four_point_string: 4,
                    five_point_string: 5, eigth_point_string: 8, ten_point_string: 10}
count = 0
for i in input_word.upper():
    for j in dict_point_count.keys():
        if i in j:
            print(f" {i} = {dict_point_count.get(j)}")
            count += int(dict_point_count.get(j))

print(f"{input_word.capitalize()} = {count} очков")
