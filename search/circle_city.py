__author__ = 'Girish'


import math

def find_devisors(number):
    yield 1
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            yield i
            yield number//i
    yield number





print(set(find_devisors(12)))