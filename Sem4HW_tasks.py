# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# from random import randint
# n = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
# print(n)
# print('число в итоговом массиве встречается', n.count(int(input('Введите искомое число: '))), 'раз')

# Вариант 2:
# list_1 = [1, 2, 3, 4, 5]
# k = int(input('Input your number: '))

# length = len(list_1)
# count = 0
# for i in range(length):
#     if list_1[i] == k:
#        count +=1

# print(count)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
# from random import randint
# input_set = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
# print(input_set)
# num = int(input('Введите искомое число: '))
# input_set = set(input_set)
# dif = 0
# if num > max(input_set):
#     print(max(input_set))
# elif num < min(input_set):
#     print(min(input_set))
# else:
#     while True:
#         if num - dif in input_set and num + dif in input_set and num - dif != num + dif:
#             print(num - dif, num + dif)
#             break
#         elif num - dif in input_set:
#             print(num - dif)
#             break
#         elif num + dif in input_set:
#             print(num + dif)
#             break
#         else:
#             dif += 1

# Вариант 2:
# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = int(input('Input your number: '))

# difference = None
# difference_list=[]
# for i in range(len(list_1)):
#     if k > list_1[i]:
#         difference = k - list_1[i]
#         difference_list.append(difference)
#     elif k == list_1[i]:
#         difference = 0
#         difference_list.append(difference)
#     else: 
#          difference = list_1[i] - k
#          difference_list.append(difference)

# min_diff = difference_list[i]
# i_min_diff = i
# for i in range(len(difference_list)):
#     if min_diff >= difference_list[i] or min_diff <= -(difference_list[i]):
#         min_diff = difference_list[i]
#         i_min_diff = i

# print(list_1[i_min_diff])


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

# scrable = {
# 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'А': 1, 'В': 1, 'Е': 1,
# 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2, 'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2,
# 'У': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4,
# 'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4, 'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8, 'X': 8, 'Ш': 8,
# 'Э': 8, 'Ю': 8, 'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
# word = str.upper(input('Введите слово: '))
# s = 0
# for i in word:
#     s += scrable[i]
# print(s, 'очков')


# Вариант 2:
# k = input('Input your word: ')

# k = k.upper()
# scrabble_dict = dict()
# scrabble_dict['A'] = 1
# scrabble_dict['E'] = 1 
# scrabble_dict['I'] = 1
# scrabble_dict['O'] = 1
# scrabble_dict['U'] = 1
# scrabble_dict['L'] = 1
# scrabble_dict['N'] = 1
# scrabble_dict['S'] = 1
# scrabble_dict['T'] = 1
# scrabble_dict['R'] = 1
# scrabble_dict['D'] = 2
# scrabble_dict['G'] = 2
# scrabble_dict['B'] = 3 
# scrabble_dict['C'] = 3 
# scrabble_dict['M'] = 3 
# scrabble_dict['P'] = 3
# scrabble_dict['F'] = 4
# scrabble_dict['H'] = 4
# scrabble_dict['V'] = 4
# scrabble_dict['W'] = 4
# scrabble_dict['Y'] = 4
# scrabble_dict['K'] = 5
# scrabble_dict['J'] = 8
# scrabble_dict['X'] = 8
# scrabble_dict['Q'] = 10
# scrabble_dict['Z'] = 10

# scrabble_dict['А'] = 1
# scrabble_dict['В'] = 1
# scrabble_dict['Е'] = 1
# scrabble_dict['И'] = 1
# scrabble_dict['Н'] = 1
# scrabble_dict['О'] = 1
# scrabble_dict['Р'] = 1
# scrabble_dict['С'] = 1
# scrabble_dict['Т'] = 1
# scrabble_dict['Д'] = 2
# scrabble_dict['К'] = 2
# scrabble_dict['Л'] = 2
# scrabble_dict['М'] = 2
# scrabble_dict['П'] = 2
# scrabble_dict['У'] = 2
# scrabble_dict['Б'] = 3
# scrabble_dict['Г'] = 3
# scrabble_dict['Ё'] = 3
# scrabble_dict['Ь'] = 3
# scrabble_dict['Я'] = 3
# scrabble_dict['Й'] = 4
# scrabble_dict['Ы'] = 4
# scrabble_dict['Ж'] = 5
# scrabble_dict['З'] = 5
# scrabble_dict['Х'] = 5
# scrabble_dict['Ц'] = 5
# scrabble_dict['Ч'] = 5
# scrabble_dict['Ш'] = 8
# scrabble_dict['Э'] = 8
# scrabble_dict['Ю'] = 8
# scrabble_dict['Ф'] = 10
# scrabble_dict['Щ'] = 10
# scrabble_dict['Ъ'] = 10

# list_of_letters = []
# for i in range(len(k)):
#     list_of_letters.append(k[i])

# list_of_items = []
# for item in scrabble_dict:
#     list_of_items.append(item)

# summ = 0
# for i in range(len(list_of_items)):
#     for j in range(len(list_of_letters)):
#         if list_of_items[i] == list_of_letters[j]:
#             summ += scrabble_dict[list_of_items[i]]

# print (summ)