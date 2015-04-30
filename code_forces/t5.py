a,b=[int(x) for x in input().split()]

left = a
ans=a
while left >= b:
    ans+=(left//b)
    temp=left//b
    left=temp+(left%b)
print(ans)
