# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55
n = int(input("Введите число: "))
while n <= 0:
    n = int(input("Укажите целое число больше нуля: "))
lst = []
for i in range(1, n + 1):
    lst.append((1 + (1 / i)) ** i)
sum = 0
for j in lst:
    sum += j
print(round(sum, 2))
