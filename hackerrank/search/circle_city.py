__author__ = 'Girish'


import math

def find_devisors(number):
    yield 1
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            yield i
            yield number//i


def predicate(number):
    memo=set()
    def func(n):
        num = number
        for i in range(int(math.sqrt(num//n))):
            temp =math.sqrt(num-(i**2))
            if temp.is_integer():
                t1=i**2
                t2=num-i**2
                if not (t1,t2) in memo:
                    memo.add((t1,t2))
                    yield t1,t2
    return func

def finding_n(number):
    w = set()
    func = predicate(number)
    ans =func(1)
    for i in ans:
        w.add(i)
    return 4+4*(len(w)-1)

for x in range(int(input())):
    a,b = [int(x) for x in input().split()]
    ans = "possible" if finding_n(a)<=b else "impossible"
    print(ans)