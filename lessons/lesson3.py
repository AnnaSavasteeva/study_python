# Определить количество вхождений одной строки в другую
# myStr = "привет мир привет друзья"
# strToFind = "привет"
#
# # Вариант 1
# words = myStr.split(" ")
# counter = 0
# for word in words:
#     if word == strToFind:
#         counter += 1
# print(counter)
#
# # Вариант 2
# print(myStr.count(strToFind))





# Генерация рандомного числа через время
# import datetime
# ms = datetime.datetime.now().microsecond
# # рандомное число от 0 до 99 (поэтому делим на 100)
# random = ms % 100
# print(random)





# Определить, есть ли в строке определенное число, и вывести номер позиции, на которой оно находится
# myList = ["word", "number", "35", "48"]
# def isDigit(lst, num):
#     for i in range(len(lst)):
#         e = lst[i]
#         if e.isdigit():
#             if int(e) == num:
#                 print(i)
# isDigit(myList, 35)




# Найти позицию второго вхождения строки в списке, либо сообщить, что второго вхождения нет
lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
def findSecond(lst, string):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == string:
            counter += 1
            if counter == 2:
                return i
    return -1
print(findSecond(lst, "qwe"))
