num = int(input())
li = [int(x) for x in input().split()]
s = set(list("aeiouy"))
lis = [ len("".join(filter(lambda x: x in s,input()))) for x in range(num)]
print("YES" if lis == li else "NO")
