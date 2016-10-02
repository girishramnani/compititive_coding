import collections as c
x,y = [ int(x) for x in input().split()]
li = [(i,ind_y)  if val=="*" else (-1,-1)  for i in range(x) for ind_y,val in enumerate(list(input())) ]
li = list(filter(lambda ti : ti[0] != -1 and ti[1] != -1,li))
first = li[0]
print(map(lambda a:a[0],li))
print(c.Counter(map(lambda a:a[0],li)))
print(c.Counter(map(lambda a:a[1],li)))
