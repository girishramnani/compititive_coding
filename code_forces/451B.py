input()
li=[int(x) for x in input().split()]
past=0
while past <(len(li)-1) and li[past] <li[past+1]: 
    past+=1
final = past
while final <len(li)-1 and li[final] > li[final+1]:
    final +=1
new_li = li[:past] + list(reversed(li[past:final+1])) +li[final+1:]


def test_sorted(li):
    for i,num in enumerate(li[:-1]):
        if num > li[i+1]:
            return False
    return True

if test_sorted(li):
    print("yes")
    print(1,1)
elif test_sorted(new_li):
    print("yes")
    print(past+1,final+1)
else:
    print("no")
