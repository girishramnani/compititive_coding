t = input()
li = [int(x) for x in input().split()]
li2 =[ sum(li[i::3]) for i in range(3)]
ind = ["chest","biceps","back"]
print(ind[li2.index(max(li2))])
