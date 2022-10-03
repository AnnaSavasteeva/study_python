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
