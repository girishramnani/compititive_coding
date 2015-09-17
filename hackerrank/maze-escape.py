y,x = [int(x) for x in input().split() ]

li = [list(input()) for i in range(5) ]

def find_dirt(grid):
    
    for i,row in enumerate(grid):
        for j,item in enumerate(row):
            if item =="d":
                return (i,j)

dirt_location = find_dirt(li)
normalized = (x - dirt_location[0], y - dirt_location[1])
y_axis = "DOWN" if normalized[1] > 0 else "UP"
x_axis = "RIGHT" if normalized[0] > 0 else "LEFT"

print(y,x)
print(normalized)
if normalized[0] !=0:
    print((x_axis+"\n")*abs(normalized[0]),end="")
else normalized[1] !=0:
    print((y_axis+"\n")*abs(normalized[1]),end="")


   
