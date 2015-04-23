from collections import Counter

word1 = input()
word2 = input()
word3 =input()

ct1 =Counter(word1)
ct2 =Counter(word2)
ct3 =Counter(word3)
ct4 =ct1+ct2
if ct4 == ct3:
    print("YES")
else:
    print("NO")
