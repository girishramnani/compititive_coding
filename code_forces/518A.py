word = input()
word2 = input()


def check(word, word2):
    count=0
    for i in range(len(word)):
        if ord(word[i]) > ord(word2[i]) :
            return False
    for i in range(len(word)):
        t = ord(word2[i]) - ord(word[i])
        if t>1:
            count+=1
    if count ==0:
        return False
    return True



if check(word,word2):
    
    i=len(word)-1
    while word[i] =="z":
        i-=1

    print(word[:i]+chr(ord(word[i])+1)+word[i+1:])
else:
    print("No such string")

