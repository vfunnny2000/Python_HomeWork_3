# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system('cls')

def conversion_binary(number):
    binary_number = ''
    while number !=0:
        binary_number = str(number%2) + binary_number
        number //=2
    return binary_number

number = int(input('Enter number:  '))
print(conversion_binary(number))    
