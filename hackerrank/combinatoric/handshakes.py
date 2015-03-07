__author__ = 'Girish'


def combinators(n,r):
    if r>n:
        return 0
    def permutation(num,r):
        ans =1
        for z in range(num ,num-r,-1):
            ans*=z
        return ans
    return permutation(n,r)//permutation(r,r)

for i in range(int(input())):
    print(combinators(int(input()),2))