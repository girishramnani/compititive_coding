import re
length = int(input())
word = input()

regex = re.compile(word);
evolutions = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

for i in evolutions:
    ans = regex.fullmatch(i)
    if ans :
        print(ans.group())
        break

