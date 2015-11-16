

input()
li=[int(x) for x in input().split()]
c =[0]*5

for i in li:
    c[i]+=1

c[1] = max(c[1]-c[3],0)
ans = c[4]+c[3]+(c[1]+(2*c[2]))/4
import math

print(math.ceil(ans))

