from collections import Counter

l1=input()
l2 = [int(x) for x in input().split()]
l3 = [int(x) for x in input().split()]
l4 = [int(x) for x in input().split()]
ct = Counter(l2)
ct2=Counter(l3)
ct3=Counter(l4)
ans1 = ct-ct2
print(list(ans1.keys())[0])
ans2=ct2 - ct3
print(list(ans2.keys())[0])
