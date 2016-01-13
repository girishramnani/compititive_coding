x,y = [int(x) for x in input().split() ]
li = [int(x) for x in input().split() ]

num=1

while num <= len(li):
    
    ne = li[num-1]
    num+=ne
    
    if num == y:
        print("YES")
        break
    
else:
    print("NO")
