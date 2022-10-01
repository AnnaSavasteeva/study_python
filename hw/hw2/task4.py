# Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt: в одной строке одно число.
n = int(input("Введите число: "))
while n <= 0:
    n = int(input("Укажите целое число больше нуля: "))

fileW = open("text.txt", "w")
for i in range(-n, n + 1):
    if i != 0:
        fileW.write(str(i) + "\n")
fileW.close()

mult = 1
fileR = open("text.txt", "r")
for line in fileR:
    mult *= int(line)
fileR.close()

print(f'Произведение: {mult}')
