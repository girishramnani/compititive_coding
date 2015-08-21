nop,max_capacity = [int(x) for x in input().split()]
lip=sorted([int(x) for x in input().split()])
ans =0
for i in range(len(lip)-1,-1,-max_capacity):
    ans+=2*(lip[i]-1)
print(ans)





