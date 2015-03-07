__author__ = 'Girish'


t = input()
li=[]
for i,x in enumerate(input().split()):
    li.append((int(x),i+1))

li= sorted(li)
max_ans  = float("-inf")

for i in range(len(li)-1):
    j=i+1
    flag =True
    while flag:
        if li[j][0]>li[i][0]:
            break
        j+=1


print(max_ans)



