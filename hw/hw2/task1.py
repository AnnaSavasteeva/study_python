# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input("Введите число: "))
dictionary = {}
while n <= 0:
    n = int(input("Укажите целое число больше нуля: "))
for i in range(1, n + 1):
    dictionary[i] = 3 * i + 1
for key, value in dictionary.items():
    print(f'{key}: {value}')
# Вариант вывода 2:
print(dictionary)
