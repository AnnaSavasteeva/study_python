# Выбрать четные числа и составить список пар: число, квадрат числа
# file = open('les5.txt', 'r')
# numbers = [int(line) for line in file]
# file.close()
# numbersSqr = [(i, i ** 2) for i in numbers if not i % 2]
# print(numbersSqr)


# map()
# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)


# filter()
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)


# zip
# users = ['user1', 'user2', 'user3']
# id = [4, 5, 6]
# combinedData = list(zip(users, id))
# print(combinedData)


# enumerate
# numberedList = list(enumerate(['one', 'two', 'three']))
# print(numberedList)


# Напишите программу, удаляющую из текста все слова, содержащие "абв"
text = 'этого абв текста все вабвс слова, содерабващие содержащие "абв"'
newText = ' '.join(list(filter(lambda w: 'абв' not in w, text.split())))
print(newText)


# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число
num = list(map(int, "0 1 2 3 4 5 7 8 9 10".split(" ")))
print([num[i]-1 for i in range(1,len(num)) if num[i]-1 != num[i-1]][0])
