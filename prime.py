__author__ = 'Girish'



import itertools


def generate_prime(n):

    counter =itertools.count(2)
    number = next(counter)
    t = set([])
    while number <n**2:
        print(number)
        t.add(number)
        counter = filter(lambda x,num=number:x%num !=0,counter)
        number = next(counter)
    return t




#better use a seive
for i in range(int(input())):
    spiral_size=int(input())
