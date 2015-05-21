import re


x,y =[int(x) for x in input().split()]
li = [ [ a for a in input().split()] for b in range(x)]
for w in li:
    w[0]=re.compile(w[0].replace("?","\d"))
ans = max(filter(lambda w: w[0].search(str(y)) != None,li),key=lambda bd:bd[1]) 

print(ans[1])
