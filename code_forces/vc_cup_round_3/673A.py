n = int(input())

li = [int(x) for x in input().split()]

def run(li):
    if li[0] > 15:
        print(15)
    else:
        for i in range(len(li)-1):
            if li[i+1] - li[i] > 15 :
                print(li[i]+15)
                break
        else:
            print(min(li[-1]+15,90))
run(li)
