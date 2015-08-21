i=2229680

while True:
    for j in [14,9,16,11,13,15,17,19,18,20]:
        if i%j!=0:
            break
    else:
        print(i)
        break
    i+=2



