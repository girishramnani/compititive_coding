__author__ = 'girish'

iteration = int(input())
ans = dict()

li = [ int(x) for x in input().split()]
for i in li:
    ans[i]=ans.get(i,0)+1
for key , value in ans.items():
    if value ==1:
        print(key)
