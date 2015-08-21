__author__ = 'girish'


def isPalindrome(number):
    checkNum=number
    new =0
    while(number>0):
        temp =number%10
        new = (new*10)+(temp)
        number = int(number/10)
        #print("temp -", temp,"new - ",new , "number-",number)

    if new == checkNum:
        return True
    return False

anslist = []
iteration = int(input())

for i in range(iteration):

    k = int(input())
    k+=1
    while True:
        if isPalindrome(k):
            anslist.append(k)
            break
        else:
            k+=1

for j in range(len(anslist)):
    print(anslist[j])


