# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import util as u

numbers = [20, 99, 126, 1084]
for num in numbers:
    print(f'Простые множители числа {num}: {u.getPrimeFactors(num)}')
