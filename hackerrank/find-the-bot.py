
addr_dict = {1 : lambda x,y,num : [x+num,y],
             2 : lambda x,y,num : [x,y+num],
             3 : lambda x,y,num : [x-num,y],
             4 : lambda x,y,num : [x,y-num] }

for i in range(int(input())):
    num = int(input())
    mul = num // 4
    tup  = [-2*mul, -2*mul]
    selector = num % 4
    for i in range(1,selector+1):
        tup = addr_dict[i](*tup,num=((mul*4)+i))
    print(" ".join(map(str,tup)))

