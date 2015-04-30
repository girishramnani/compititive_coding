x,i =[int(w) for w in input().split()]

li =list(input())


for a in range(i):
    bol=False
    for b in range(x-1):
        if(bol):
            bol=False
            continue
        if(li[b] =="B"):
            if (li[b+1] =="G"):
                li[b],li[b+1]=li[b+1],li[b]
                bol=True



print("".join(li))
