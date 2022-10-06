import math as m


def isEven(num):
    return num % 2 == 0


def getMultList(lst):
    multLst = []
    lstLen = len(lst)
    lastEl = lstLen - 1
    for i in range(m.ceil(lstLen / 2)):
        multLst.append(lst[i] * lst[lastEl - i])
    return multLst


def getNegaFibonacciNums(n):
    if n <= 2:
        return 0
    else:
        fibRight = getPositiveFibNums(n)
        fibLeft = getNegativeFibNums(n)
        fibLeft.reverse()
        fibLeft.pop()
        fibLeft.extend(fibRight)
        return fibLeft

def getPositiveFibNums(n):
    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[(len(fib) - 1)] + fib[(len(fib) - 2)])
    return fib

def getNegativeFibNums(n):
    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[(len(fib) - 2)] - fib[(len(fib) - 1)])
    return fib
