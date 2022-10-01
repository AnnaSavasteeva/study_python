# Посчитать, сколько раз символ встречается в строке
# myString = input("Введите свой текст: ")
# mySymbol = input(f'Укажите, какой символ найти в строке "{myString}": ')
# counter = 0
# for s in myString:
#     if s == mySymbol:
#         counter += 1
# print(f'Символ {mySymbol} встречается в строке "{myString}": {counter}')




# Дано количество секунд. Вывести в виде "дни:часы:минуты:секунды"
# seconds = int(input("Укажите количество секунд: "))

# Вариант 1
# minutes = seconds // 60
# seconds -= minutes * 60
# hours = minutes // 60
# minutes -= hours * 60
# days = hours // 24
# hours -= days * 24

# Вариант 2
# minutes, seconds = seconds // 60, seconds % 60
# hours, minutes = minutes // 60, minutes % 60
# days, hours = hours // 24, hours % 24
#
# print(f'{days} : {hours} : {minutes} : {seconds}')




# Дано число 5. Вывести для него последовательность: 1, -3, 9, -27, 81
for i in range(5):
    print((-3)**i, end=" ")
