num = int(input())

database = dict()

for i in range(num):
    word = input()
    if word not in database:
        print("OK")
        database[word] = 0
    else:
        index = database[word]+1
        database[word]+=1
        print(word+str(index))
