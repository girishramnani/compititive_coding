i = int(input())
w = input()
ss = set(w)

def check(ww):
    return sum(map(lambda x: int(x),ww[:len(ww)//2])) == sum(map(lambda x:int(x),ww[len(ww)//2:]))


def check2(ww):

    if len(ss) == 1:
        if'4' in ss or '7' in ss:
            return check(ww)
        return False
    elif len(ss) ==2 :
        if '4' in ss and '7' in ss:
            return check(ww)
        return False
    return False

if check2(w):
    print("YES")
else:
    print("NO")


