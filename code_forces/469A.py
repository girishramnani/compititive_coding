n = int(input())
s = set([ int(x) for x in input().split()][1:])
s2 = s.union(set([int(x) for x in input().split()[1:]]))

if len(s2) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

