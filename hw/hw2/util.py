import datetime


def getRandomInt(randomRange):
    return datetime.datetime.now().microsecond % randomRange


def shuffleList(list):
    shuffledLst = []
    while (len(list) != 0):
        index = getRandomInt(len(list))
        el = list[index]
        shuffledLst.append(el)
        list.remove(el)
    return shuffledLst
