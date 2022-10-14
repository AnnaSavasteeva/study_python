# Task 1
def getStrNoExp(num):
    return str('{:f}'.format(num)).rstrip('0')

def getFractionalSymbolsAmount(num):
    return len(getStrNoExp(num).rstrip('0').split('.')[1])



# Task 2
def getPrimeFactors(num):
    factors = []
    divider = 2
    while divider ** divider <= num:
        if num % divider == 0:
            factors.append(divider)
            num //= divider
        else:
            divider += 1
    if num > 1:
        factors.append(num)
    return factors



# Task 3
def countValueInList(lst, value):
    counter = 0
    for i in range(len(lst)):
        if lst[i] == value:
            counter += 1
    return counter


def getDistinctValues(lst):
    return list(filter(lambda el: countValueInList(lst, el) == 1, lst))
