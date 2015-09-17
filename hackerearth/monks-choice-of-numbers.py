from __future__ import print_function

def work(num):
    ans=0
    while num:
        ans+=(num&1)
        num = num >> 1
    return ans

for i in range(int(raw_input())):
    x,y =[int(w) for w in raw_input().split()]
    li = [int(w) for w in raw_input().split()]
    print(sum(sorted(map(work,li),reverse=True)[:y]))
