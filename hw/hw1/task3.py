# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).
axisNum = int(input("Укажите номер четверти: "))
if axisNum == 1:
    print("x > 0, y > 0")
elif axisNum == 2:
    print("x < 0, y > 0")
elif axisNum == 3:
    print("x < 0, y < 0")
elif axisNum == 4:
    print("x > 0, y < 0")
else:
    print("Такой четверти не существует")
