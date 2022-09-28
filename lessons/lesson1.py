# print("Проверить, является ли число квадратом другого:")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print((a ** 2 == b) or (b ** 2 == a))

# print("Найти максимальное из заданных 5 чисел:")
# lst = [1, 40, 25, -13, 0]
# print(lst)
# max = lst[0]
# for i in lst:
#     if i > max:
#         max = i
# print("Максимальное:", max)

# print("Найти максимальное из введенных пользователем 5 чисел:")
# lstFromUser = []
# for i in range(5):
#     num = int(input("Введите число: "))
#     lstFromUser.append(num)
# maxNum = lstFromUser[0]
# for i in range(1, 5):
#     if maxNum < lstFromUser[i]:
#         maxNum = lstFromUser[i]
# print(lstFromUser)
# print(maxNum)

# print("Принимает число N и выводит диапазон чисел от -N до N:")
# n = int(input("Введите число: "))
# for i in range(-n, n + 1):
#     print(i, end = " ")

# print("Принимать на вход дробь и показывать первую цифру дробной части:")
# myFloat = float(input("Введите дробь: "))
# fractionalPart = int(myFloat * 10 % 10)
# print(fractionalPart)

# print("Найти число, кратное 5 и 10 или 15, но не 30")
# num = int(input("Введите число: "))
# isFiveTen = (num % 5 == 0) and (num % 10 == 0)
# isFifteenThirty = (num % 15 == 0) and (num % 30 != 0)
# print(isFiveTen or isFifteenThirty)

# print("Проверка истинности утверждения: (X ⋁ Y ⋁ Z) = X ⋀ Y ⋀ Z для всех значений предикат")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             # print((x, y, z), ':', (not(x or y or z)) == (not x and not y and not z))
#             print(f'{x, y, z} : {(not(x or y or z)) == (not x and not y and not z)}')

# print("Сложить числа вещественного числа")
# n = input("Введите число: ")
# res = 0
# for i in n:
#     if i != "." and i != ",":
#         res += int(i)
# print(res)

# print("Проверить, является ли строчка палиндромом:")
# Вариант 1
# myString = "abba"
# res = "Палиндром"
# for i in range(len(myString) // 2):
#     if myString[i] != myString[-1-i]:
#         res = "Не палиндром"
#         break
# print(res)

# Вариант 2
# myString2 = "abba"
# reversedString = myString2[::-1]
# if myString2 == reversedString:
#     print("Палиндром")
# else:
#     print("Не палиндром")

print("Написать прогу, которая выводит нечетные числа из списка, и останавливается, если встречает число 554:")
myNumbers = [1, 67, 88, -554, 1034, 554, 345, 298, 2, 0, -5]
for i in myNumbers:
    if i == 554:
        break
    elif i % 2 == 0:
        print(i, end=" ")
print()
print(1, 2, 3, 4, 5, sep="|")
