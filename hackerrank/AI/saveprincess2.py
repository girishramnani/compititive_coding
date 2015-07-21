

def make_grid(size):
    input()
    grid=[]
    for i in range(size):
        grid.append(list(input()))
    return grid

def find_princess_bot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
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

flag=0
if normalized[0] !=0:
    print(x_axis+"\n",end="")

elif normalized[1] !=0 :
    print(y_axis+"\n",end="")
