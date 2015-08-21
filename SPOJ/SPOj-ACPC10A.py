__author__ = 'girish'


def CheckForZeros(li):
    for i in li:
        if i != 0:
            return False
    return True

resultList = []
while True:

    k = input().rsplit(" ", 2)
    for dum2 in range(len(k)):
        k[dum2] = int(k[dum2])

    if CheckForZeros(k):
        break

    elif (k[0] - k[1]) == (k[1] - k[2]):
        resultList.append("AP " + str((k[2] + (k[1] - k[0]))))
    else:
        resultList.append("GP {0}".format(int((k[2] * (k[1] / k[0])))))

for dummy in range(len(resultList)):
    print(resultList[dummy])




