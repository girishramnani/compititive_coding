__author__ = 'Girish'

import math

t = int(input())

for i in range(1,10):
    t2 = pow(i,t)
    if int(math.log10(t2))+1 ==t:
        print(t2)

