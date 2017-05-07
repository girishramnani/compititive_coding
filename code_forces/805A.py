a,b = [int(x) for x in input().split()]
if a==b:
    print(a)
elif a % 3==0 and b % 3==0 and abs(a-b)==3:
    print(3)
else:
    print(2)
