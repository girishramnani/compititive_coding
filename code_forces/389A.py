input()
li = [int(x) for x in input().split()]
li.sort()
mi = min([ li[i]-(li[i]//li[i-1]-1 if (li[i]/li[i-1]).is_integer() else li[i]//li[i-1])*li[i-1] if li[i]>li[i-1] else li[i] for i in range(1,len(li))])
print(mi*len(li))
