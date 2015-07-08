word = input().lower()

find="codeforces"
j=0
import pdb; pdb.set_trace()
for i in range(len(word)):
    if find[j]==word[i]:
        j+=1
if j==len(find):
    print("YES")
else:
    print("NO")


