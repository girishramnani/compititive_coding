image ="""
0000000000
0111111100
0000111100
0000111100
0001111100
0000111100
0001100000
0000000000
0000000000
"""
new_image = image[:]
new_image = image.strip().split()
image = image.strip().split()


def make_list(li):
    return [ list(map(int,row)) for row in li ]


image = make_list(image)
new_image = make_list(image)

delta = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

for i,row in enumerate(image):
    for j in range(len(row)):
        plausable = []
        for d_x,d_y in delta:
            
            if (-1 < j+d_y < len(row)) and (-1 < i+d_x < len(image)):
                plausable.append(image[i+d_x][j+d_y])
        if all(plausable):
            new_image[i][j] = 1
        else:
            new_image[i][j] = 0
d = "\n".join(map( lambda x: "".join(map(str,x)),new_image))
print(d)
print(d.count("1"))
