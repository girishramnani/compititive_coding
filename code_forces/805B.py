import itertools as it
t = int(input())
cc = it.cycle("aabb")
print("".join([ next(cc) for _ in range(t)]))



