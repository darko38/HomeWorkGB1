# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
from random import random

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# a=int(input('Введите первое число: '))
# b=int(input('Введите второе число: '))
# if a*a==b or b*b==a:
#     print('Yes')
# else:
#     print('No')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# 2.1
# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# c = int(input('Введите третье число'))
# d = int(input('Введите четвертое число'))
# e = int(input('Введите пятое число'))
# if a > b:
#     max = a
# else:
#     max = b
# if max > c:
#     max = max
# else:
#     max = c
# if max > d:
#     max = max
# else:
#     max = d
# if max > e:
#     max = max
# else:
#     max = e
# print(max)


# 2.2
# t = []
# for i in range(5):
#   m=int(input('Введите число: '))
#   t.append(m)
# max_t=t[0]
# for i in t:
#     if i > max_t:
#         max_t = i
# print(max_t)
# print(t)

# 2.3
# t = []
# for i in range(5):
#   t.append(int(input('Введите число: ')))
#   max_t=t[0]
# for i in t:
#     if i > max_t:
#         max_t = i
# print(max_t)

# Разница между 'for i in my_list' и 'for i in range(len(my_list))
# my_list = [4, 89, 432, 45, 22, 29]
# print(my_list)
# for i in range(len(my_list)):
#     print(i)
# for i in my_list:
#     print(i)

# Как работает append
# animals = ['fox', 'frog', 'monkey']
# print(animals)
# animals.append('crocodile')
# print(animals)
# Заполнение списка через append
# my_list = []
# for i in range(5):
#     my_list.append(int(input('Введите число: ')))
# print(my_list)

# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#
# *Примеры:*
#
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# 3.1
# a = float(input('Введите число: '))
# if a == int(a):
#     print('No')
# else:
#     b=int(a*10)%10
#     print(b)

# 3.2
# a=int(float(input('Введите число: '))*10)%10
# print(a)

# import random
# # Заполнение массива через указание количества чисел в нём
# size = int(input('Введите размер массива: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0,100))
# print(my_list)