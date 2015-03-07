__author__ = 'Girish'


for x in range(int(input())):
    word =input()
    rev_word = word[::-1]
    for i in range(1,len(word)):
        if abs(ord(word[i])-ord(word[i-1]))!=abs(ord(rev_word[i])-ord(rev_word[i-1])):
            print("Not Funny")
            break
    else:
        print("Funny")
