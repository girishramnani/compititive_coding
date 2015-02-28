__author__ = 'Girish'


t =input()

li = [int(x) for x in input().split()]

def left(li,i):
    ans =float("inf")
    index=0
    for w in range(i):
        if li[w]>li[i] :
            if ans >li[w]:
                ans=li[w]
                index=w
    return index+1 if ans !=float("inf") else 0

def right(li,i):
    ans =float("inf")
    index=0
    for w in range(i+1,len(li)):
        if li[w]>li[i] :
            if ans >li[w]:
                ans=li[w]
                index=w
    return index+1 if ans !=float("inf") else 0

ans = max((left(li,i)*right(li,i))for i in range(1,len(li)-1))
print(ans)



