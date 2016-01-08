n,m = [ int(x) for x in input().split()]
bulbs = set([])
for i in range(n):
    for j in map(int,input().split()[1:]):
        bulbs.add(j)

if len(bulbs)>=m:
    print("YES")
else:
    print("NO")


