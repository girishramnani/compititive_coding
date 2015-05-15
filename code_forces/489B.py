
n = input()
li1 =sorted([ int(x) for x in input().split()])
n2 = input()
li2=sorted([int(x) for x in input().split()])
count=0
for i,num in enumerate(li1):
    j=0
    while j<len(li2):
        if abs(num-li2[j]) <=1:
            count+=1
            del(li2[j])
            break
        elif num+1 <li2[j]:
            break
        j+=1
print(count)    
            
                

