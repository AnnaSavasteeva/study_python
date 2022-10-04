# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import util

lst = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(lst)):
    if not util.isEven(i):
        sum += lst[i]
print(sum)
