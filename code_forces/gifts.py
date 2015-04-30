

x,y =[int(w) for w in input().split()]
li =[ int(xx) for xx in input().split()]
li.sort()
mi = float("inf")
for i in range(y-x+1):
    now =  li[i+x-1]-li[i]
    if now < mi:
        mi = now


print(mi)
        
    
