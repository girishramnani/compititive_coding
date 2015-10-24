while True:
    word = input()
    if word=="END":
        break
    count = 1
    while word!="1":
        word = str(len(word))

        count+=1
    print(count)
        
