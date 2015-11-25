x,y = [int(x) for x in input().split()]
pi =[int(x) for x in input().split()]

d=dict()
for i,val in enumerate(pi):
    x = d.get(val,[]) 
    x.append(i+1)
    d[val] = x

pi.sort()
si=0
sol=[]
n=0
while pi:
    ins = pi.pop(0)   
    if ins+si > y:
        break
    elif ins+si <=y:
        si+=ins
        sol.append(d[ins].pop())
    
print(len(sol))
if sol:
    print(" ".join(map(str,sorted(sol))))
   

