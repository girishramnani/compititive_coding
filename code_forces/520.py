

def ans(x,y):
    moves = [lambda a:a*2,lambda b :b-1]
    lis = [x]
    count=0
    import pdb
    pdb.set_trace()
    while lis:
        ww = lis.pop(0)
        if ww ==y:
            print(count)
            break
        for i in moves:
            lis.append(i(ww))
        count+=1

print(ans(4,6))
