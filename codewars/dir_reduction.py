__author__ = 'Girish'


def dirReduc(arr):
    stack=[arr[0]]
    for i in arr[1:]:
        try:
            word = stack[-1]
        except:
            word=""

        if (word == "NORTH" and i =="SOUTH") or (i == "NORTH" and word =="SOUTH"):
            stack.pop()
        elif (word == "EAST" and i =="WEST") or (i == "EAST" and word =="WEST"):
            stack.pop()
        else:
            stack.append(i)
    return stack


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))