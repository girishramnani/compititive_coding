__author__ = 'girish'


answerList=[]

def splitAndConvert(k):
    k = k.split(" ")
    for i in range(len(k)):
        k[i]= int(k[i])
    return k

iteration = int(input())
for dummy in range(iteration):
    k=int(input())

    first = input()
    first = splitAndConvert(first)
    first.sort()

    second = input()
    second = splitAndConvert(second)
    second.sort()
    sum1=0
    for i in range(len(first)):
        sum1+=(first[i]*second[i])
    answerList.append(sum1)


for z in range(len(answerList)):
    print(answerList[z])

