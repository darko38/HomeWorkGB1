# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# from decimal import Decimal
# a=Decimal(float(input('Введите число: ')))
# b=0
# while float(a) != int(a):
#     a *= 10
# else:
#     while a> 0:
#         dig = a % 10
#         b = b + dig
#         a = a//10
# print(int(b))

# 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.
import decimal
# N = int(input('Введите число: '))
# my_list = []
# for i in range(1, N+1):
#     my_list.append((1+1/i)**i)
# sum_my_list=0
# for i in my_list:
#     sum_my_list += i
# print(my_list)
# print(sum_my_list)

# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.
# import random
# size = int(input('Введите размер массива: '))
# my_list = []
# for i in range(size):
#     my_list.append(random.randint(0,100))
# print(my_list)
# my_new_list=[]
# for i in range(size):
#     my_new_list.append(my_list[-i])
# print(my_new_list)

