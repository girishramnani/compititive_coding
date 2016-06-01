n = int(input())
li = [int(x) for x in input().split()]
mi = 1
ma = n
ind_ma = li.index(ma)
ind_mi = li.index(mi)



if ind_ma == n-1 or ind_mi == 0:
    print(n-1)
else:
    dma = (n-1) - ind_ma
    dmi = (n-1) - ind_mi
    print(max([dma,dmi,ind_ma,ind_mi]))

