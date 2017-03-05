word = input()
l = int(input())
if len(word)%l != 0:
    print("NO")
else:
    for i in range(0,len(word),len(word)//l):
        w = word[i:i+len(word)//l]
        if w != w[::-1]:
            print("NO")
            break
    else:
        print("YES")
