li=[int(x) for x in input().split()]
dt=li[0]
lit = list(li)
t = min(li)
li=list(map(lambda f:f-t,li))
cn=0
if sum(map(lambda w:w%3,li))==4 and all(lit):
    cn=1
ans=t
for i in li:
    ans+=(i//3)
print(ans+cn)
