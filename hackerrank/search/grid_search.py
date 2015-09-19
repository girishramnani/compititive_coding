row = int(input())
input()
grid = [[int(x) for x in input().split()] for j in range(row)]

possible={(j,i) for i in range(len(grid[0])) for j in range(row) if grid[j][i]  }


def neighbour(grid,i,j):
    possible_moves = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
    width,height =len(grid[0]),len(grid)
    for x,y in possible_moves:
        if 0 <= i+x < height and 0<= y+j < width and grid[x+i][y+j]:
            yield i+x , y+j

            
            


max_c = 0
while possible:
    queue = [possible.pop()]
    done =set([queue[0]])

    count=1
    while queue:
        point = queue.pop(0)
        for x,y in neighbour(grid,point[0],point[1]):
            if grid[x][y] and (x,y) in possible and (x,y) not in done:
                queue.append((x,y))
                done.add((x,y))
                count+=1
    if max_c < count:
        max_c = count
    possible.difference_update(done)
print(max_c)