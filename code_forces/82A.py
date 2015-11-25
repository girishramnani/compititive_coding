import math
def test(n):
    d =["Sheldon","Leonard","Penny","Rajesh","Howard"]
    if n <=5:
        return d[n-1]
    i=1
    ans=1
    newans=1
    while ans < n:
        newans+=((2**(i-1))*5)
        if newans > n:
            break
        ans = newans
        i+=1
    return d[((n%ans)//(2**(i-1)))]

print(test(int(input())))
