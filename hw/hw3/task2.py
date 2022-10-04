# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import util as u

lstOdd = [2, 3, 4, 5, 6]
lstEven = [2, 3, 5, 6]

print(u.getMultList(lstOdd))
print(u.getMultList(lstEven))
