# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import os
os.system('cls')

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))



# import os
# os.system('cls')

# from random import uniform

# def get_real_nums (n, frst, last):
#     return [round(uniform(frst,last), 2) for i in range(n)]

# def find_diff(mynums):
#     nums = [round(x - int(x), 2) for x in (mynums)]
#     return max(nums) - min(nums)

# n = 5
# frst = 1
# last = 10
# mynums = get_real_nums(n, frst, last)

# print (mynums)
# print(find_diff(mynums))




