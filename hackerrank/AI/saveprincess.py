

def make_grid(size):
    grid=[]
    for i in range(size):
        grid.append(list(input()))
    return grid

def find_princess_bot(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='p':
                princess = (j,i)
            elif grid[i][j] =='m':
                bot = (j,i)
    return princess,bot

grid = make_grid(int(input()))
princess,bot = find_princess_bot(grid)

normalized = (princess[0] - bot[0], princess[1] - bot[1])

y_axis = "DOWN" if normalized[1] > 0 else "UP"
x_axis = "RIGHT" if normalized[0] > 0 else "LEFT"

if normalized[0] !=0:
    print((x_axis+"\n")*abs(normalized[0]),end="")
if normalized[1] !=0:
    print((y_axis+"\n")*abs(normalized[1]),end="")
