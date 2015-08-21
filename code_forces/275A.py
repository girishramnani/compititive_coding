lix = [[int(x) for x in input().split()] for y in range(3) ]
bulbs = [[ "1" for x in range(3)] for y in range(3)]
moves = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
for x in range(3):
    for y in range(3):
        if lix[x][y] & 1:
            for a,b in moves:
                if (x+a <3 and x+a>-1) and (y+b <3 and y+b>-1):
                    bulbs[x+a][y+b] ="0" if int(bulbs[x+a][y+b]) else "1"


print("\n".join(["".join(li) for li in bulbs]))



