

n,m=map(int,input().split())
s=input()
ans,a,b,l=0,0,0,0
for i in s:
    if i=='a':
         a+=1
    else:
         b+=1
    if min(a, b)>m:
        if s[l]=='a':
             a-=1
        else:
             b-=1
        l+=1
    else:
         ans+= 1
print(ans)