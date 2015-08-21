import itertools

ind={'+':1,'-':-1}
def map_func(a):
   ind2=ind
   return ind2.get(a,a)



li = sum(map(lambda a: 1 if a=="+" else -1 , input()))
li2 =list(map(map_func,input()))
try:
    index = li2.index("?")
    ans_li21 = list(filter(lambda x: x!="?",li2))
    ans_li2 = sum(ans_li21)
    iterations=len(li2)-len(ans_li21)
    liz = [ans_li2]
    li2=[]
    for i in range(iterations):
        while liz:
            num = liz.pop()
            li2.extend((num+1,num-1))
        liz=li2
        li2 =[]
    print("{:.12f}".format(len(list(filter(lambda x:x==li,liz)))/len(liz)))


except ValueError:
    if sum(li2)==li:
        print("{:.12f}".format(float(1)))
    else:
        print("{:.12f}".format(0.0))
