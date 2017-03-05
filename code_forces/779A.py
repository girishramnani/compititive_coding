n = int(input())
li1 = [int(x) for x in input().split()]
li2 = [int(x) for x in input().split()]
cnt = [ 0 for x in range(6)]
for i in li1:
    cnt[i]+=1
for i in li2:
    cnt[i]-=1

for i in cnt:
    if i % 2 != 0:
        print(-1)
        break
else:
    ans = sum([ abs(x) for x in cnt])
    print(ans//4)

