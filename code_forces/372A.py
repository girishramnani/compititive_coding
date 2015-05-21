num = int(input())
li = sorted([int(input()) for i in range(num)])
done =set([])
pocketed=0
for i,kangro in enumerate(li):
    for j in range(i,len(li)):
        if i not in done and j not in done:

            if li[j] >=2*kangro:
                pocketed+=1
                done.add(kangro)
                done.add(li[j])
                break


print(len(li)-pocketed-1)

