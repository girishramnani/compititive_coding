
from __future__ import print_function
for i in range(int(raw_input())):
    x,y = [int(w) for w in raw_input().split()]
    
    print(list(bin(x^y)).count("1"))

