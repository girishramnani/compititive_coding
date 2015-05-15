row,column =[int(x) for x in input().split()]
rowset=set([])
columnset=set([])
rowdone=0
columndone=0
for i in range(row):
    li = list(input())
    for j,w in enumerate(li):
        if w=="S":
            rowset.add(i)
            columnset.add(j)
ans=0
for i in range(row):
    if i not in rowset:
        ans+=(column-columndone)
        rowdone+=1
       
for i in range(column):
    if i not in columnset:
        ans+=(row-rowdone)
        columndone+=1
print(ans)

