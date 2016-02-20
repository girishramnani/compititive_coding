import pprint
i = int(input())

li = [[ch for ch in input()] for _ in range(i)] 
trans_fil = [[ch for ch in lit if ch == 'C' ] for lit  in li ]  
fil =  [[ch for ch in lit if ch == 'C' ] for lit  in map(list,zip(*li)) ] 
rows =  sum(map(lambda x : (len(x)*(len(x)-1))//2,fil))
columns =  sum(map(lambda x : (len(x)*(len(x)-1))//2,trans_fil))
print(rows+columns)




