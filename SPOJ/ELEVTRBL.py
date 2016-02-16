f,s,g,u,d = [int(i) for i in input().split()]


q = [(s,0)]
count =0
visited =set([s])

while q:
    data,btn = q.pop(0)
    if data == g:
        print(btn)
        break
    for i in [u,-1*d]:
        nb = data+i
        if nb not in visited and nb >=1 and nb <= f:
            q.append((nb,btn+1))
            visited.add(nb)
    
else:
    print("use the stairs")




