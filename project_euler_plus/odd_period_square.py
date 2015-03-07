__author__ = 'Girish'
import math

def pell_coefficient(num):
    sq = int(math.sqrt(num))
    if num ==sq**2:
        return -1
    m0=0
    m1=0
    d0=1
    d1=0
    a0=int(sq)
    a1=0
    li=0
    li+=1
    while a1!=2*sq:
        m1=(d0*a0)-m0
        d1 = int((num - (m1**2) )/ d0)
        a1 = int((sq+m1)/d1)
        m0=m1
        d0=d1
        a0=a1
        li+=1

    return li

ans=0

for i in range(2,int(input())+1):
    if (pell_coefficient(i)-1) & 1 :
        ans+=1

print(ans)

