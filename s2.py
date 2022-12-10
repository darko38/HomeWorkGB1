# Команда split
# numbers = input('Введите число: ')
# count = int(input('Введите точность: '))
# print(numbers)
# numbers = numbers.split('.')
# print(numbers)
# print(numbers[0] + '.' + numbers[1][0:count])

# Срез
# numbers = input('Введите строку: ')
# print(numbers[0:3])
# print(numbers[0:-4])

# numbers = float(input('Введите число: '))
# def digit_after_dot_counter(num:float):
#     count = 0
#     div = 1
#     while True:
#         if num * div != int(num * div):
#             count += 1
#             div *= 10
#         else: break
#     return count

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#
# *Примеры:*
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# a = int(input('Введите число: '))
# my_list = []
# if a>0:
#     for i in range(-a, a+1):
#         my_list.append(i)
# else:
#     for i in range(a, -a+1):
#         my_list.append(i)
# print(my_list)

# a = [1,2,3,4]
# print(a)
# print(*a)
# print(*a, sep=', ')
# print(*a, end=' конец строки')
# print(*a, end='\n')
# print(*a, sep=', ', end=' конец строки')

# 2. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# number = int(input('Введите число: '))
# if (number%10 == 0 or number%15 == 0) and number%30 !=0:
#     print('Условие выполнено')
# else:
#     print('Условие не выполнено')

# 3. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число: '))
# Первое решение 3 задачи:
# my_list=[]
# for i in range(N):
#     my_list.append((-3)**i)
# print(*my_list, sep=', ')

# Второе решение 3 задачи:
my_list=[1]
for i in range(N-1):
    my_list.append(my_list[i]*(-3))
print(my_list)