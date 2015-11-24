__author__ = 'girish'



def find(n):
    li = list(map(int,n))
    all = max(li)
    ansL = [[] for _ in range(all)]
    now_max=li[0]
    for i in li:
        if now_max < i :
            now_max = i

        for it in range(now_max):
            if it < i:
                ansL[it].append("1")
            else:
                ansL[it].append("0")

    for w in range(len(ansL)):
        ansL[w] = "".join(ansL[w])
    print(len(ansL))
    return " ".join(ansL)

print(find(input()))

