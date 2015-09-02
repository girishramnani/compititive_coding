

def gcd(num1,num2):
    if num1==0:
        return num2
    return gcd(num1%num2,num1)


def lcm(num,num2):
    return(num*num2)//gcd(num,num2)
print(lcm(6,4))
