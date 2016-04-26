# all exterior angle add up to 360 and as regular polygon has all sides
# equal that means angle should be 360/n i.e divisible by 360
t = [ (lambda x: "NO" if 360%(180-x) != 0  else "YES")(int(input())) for _ in range(int(input()))]
print("\n".join(t))
