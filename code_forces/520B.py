count=0
m,n = [int(x) for x in input().split()]

queue=[(m,0)]
visited=set([m])
minstep=float("inf")
while queue:
    num,step = queue.pop(0)
    if num==n:
        if step < minstep:
            minstep = step
    if num > n:
        adder = num-n
        queue.append((n,step+adder))

    else:
        for adder in [lambda x:x-1,lambda x:x*2]:
            ne = adder(num)
            
            if ne==n or (ne not in visited and ne >0):
                queue.append((ne,step+1))         
                visited.add(ne)
print(minstep)       

