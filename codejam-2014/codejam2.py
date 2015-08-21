__author__ = 'Girish'
import math
def dp(num , deno =0):
    if num==1:
        return 1
    return min(2**deno+dp(math.ceil(num/2),deno+1),1+dp(num-1,deno+1))


for i in range(int(input())):
    t = input()
    li =[int(x) for x in input().split()]
    ans = max(li)
    print("Case #{}: {}".format(i+1,dp(ans)))

