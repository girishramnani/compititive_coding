input()

li = [int(x) for x in input().split()]
change =[0,0]

for value in li:
    if value == 25:
        change[0]+=1
    elif value == 50:
        if change[0]>0:
            change[0]-=1
            change[1]+=1
        else:
            print("NO")
            break
    else:
        if change[0]>0:
            if change[1] > 0:
                
                change[0]-=1
                change[1]-=1
            elif change[0]>2:
                change[0]-=3
            else:
                print("NO")
                break
                
        else:
            print("NO")
            break
else:
    print("YES")
            
            
            
