# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import random
# import random
# my_list = []
# l = int(input('Введите длину списка: '))
# for i in range(l):
#     my_list.append(random.randint(-100,100))
# print(my_list)
# n = 0
# for i in range(len(my_list)):
#     if i%2 == 1:
#         n += my_list[i]
# print(f'Сумма элементов с нечеткими индексами равна {n}')
import random


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# my_list = []
# count = int(input('Введите длину списка: '))
# for i in range(count):
#     my_list.append(random.randint(0,100))
# print(my_list)
# c = []
# if len(my_list)%2==0:
#     for i in range(len(my_list) // 2):
#         c.append(my_list[i]*my_list[-(i+1)])
# else:
#     for i in range(len(my_list) // 2 + 1):
#         c.append(my_list[i] * my_list[-(i + 1)])
# print(c)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] = > 0.19

# my_list = []
# count = int(input('Введите длину списка: '))
# for i in range(count):
#     my_list.append(float(input(f'Введите {i} элемент списка: ')))
# my_list1 = []
# b = 0
# for i in range(len(my_list)):
#     if float(my_list[i])!=int(my_list[i]):
#         b=str(my_list[i])
#         b=b.split('.')
#         b = float('0'+ '.' + b[1][0:])
#         my_list1.append(b)
# print(my_list1)
# max_element=my_list1[0]
# min_element=my_list1[0]
# for i in range(len(my_list1)):
#     if my_list1[i]>max_element:
#         max_element=my_list1[i]
#     if my_list1[i]<min_element:
#         min_element=my_list1[i]
# difference_maxmin=float(max_element)-float(min_element)
# print(max_element)
# print(min_element)
# print(f'Разницу между максимальным и минимальным значением дробной части элементов равна {difference_maxmin}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроенных методов (арифметически).
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
# c = int(input('Введите число: '))
# my_list = []
# while c!=0:
#     my_list.append(c % 2)
#     c=c//2
# my_list=my_list[::-1]
# my_list=''.join(str(i) for i in my_list)
# print(my_list)


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# count = int(input('Введите длину последовательности: '))
# a = 0
# b = 1
# c = 0
# d = -1
# my_list = []
# for i in range(0, count*2+2):
#     if i == 0:
#         next = i
#         my_list.append(i)
#     elif i == 1:
#         next = i
#         nenext = -i
#         my_list.append(i)
#         my_list.insert(0, -i)
#     else:
#         next = a + b
#         nenext = c - d
#         a = b
#         b = next
#         c = d
#         d = nenext
#         my_list.append(next)
#         my_list.insert(0, nenext)
#     print(my_list)