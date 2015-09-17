

def gcd(num1,num2):
    if num2==0:
        return num1
    return gcd(num2,num1 % num2)


def lcm(num,num2):
    return(num*num2)//gcd(num,num2)

for i in range(int(input())):
    ans =2
    for i in range(2,int(input())+1):
        ans = lcm(i,ans)
    print(ans)
