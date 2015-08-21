nos = int(input())

player1 = set([])
player2 = set([])
dec1 = [int(x) for x in input().split()][1:]
dec2 = [int(x) for x in input().split()][1:]

count=0
while dec1 and dec2:
    
    card1  = dec1.pop(0)
    card2 = dec2.pop(0)
    if card1 > card2:
        dec1.append(card2)
        dec1.append(card1)
    else:
        dec2.append(card1)
        dec2.append(card2)
    count+=1
    t2 = tuple(dec2)
    t1 = tuple(dec1)
    if t1 in player1 and t2 in player2:
        print(-1)
        break
    else:
        player1.add(t1)
        player2.add(t2)
else:
    print(count,1 if dec1 else 2)
        
    


