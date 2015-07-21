import xml.etree.ElementTree as et

li = "\n".join(input() for _ in range(int(input())))


root = et.ElementTree(et.fromstring(li))
root  = root.getroot()

def find_depth(root):
    
    max_d = 0
    for i in root:
        if len(i):
            depth = find_depth(i)+1
            if depth > max_d:
                max_d=depth
    return max_d
max_d =find_depth(root)
print(max_d)
print(len(root))
print(max_d + (1 if max_d!=0 and len(root)!=1 else 0) )
