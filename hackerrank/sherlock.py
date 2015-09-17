import pdb

pdb.set_trace();
lent,query = [int(x) for x in input().split()]
li = [int(x) for x in input().split()]

ans_li = [[1 for _ in range(len(li))] for _ in range(len(li))]

for i in range(len(ans_li)):
    past_max = li[i]
    current_val=1
    for j in range(i+1,len(ans_li)):
        if past_max > li[j]:
            ans_li[i][j] = current_val
            past_max = li[j]
        elif past_max ==li[j]:
            ans_li[i][j] = ans_li[i][j-1]+1
            current_val = ans_li[i][j]
        
            
import pprint
pprint.pprint(ans_li)
