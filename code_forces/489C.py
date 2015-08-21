x,y = [ int(x) for x in input().split()]
ans=""
ans2=""
su=y
tempy=y
tempx=x
def can(m,s):
    return  s>=0 and s<=9*m
x2=int(x)

for i in range(x):
    for j in range(10):
       if can(x-1,su-j):
            ans+=str(j)
            x-=1
            su-=j
            break
i=0
j=0
for i in range(x2):
    for j in range(9,-1,-1):
        if can(x2-1,y-j):
            ans2+=str(j)
            x2-=1
            y-=j
            break

if x==1 and tempy==0:
    print(0,0)
elif len(ans) ==0 :
    print(-1,-1)
elif int(ans) == 0:
    print(-1,-1)
elif int(ans2) < int(ans) :
    print(ans,ans)
else:
    print(int(ans),ans2)
