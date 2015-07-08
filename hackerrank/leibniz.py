for k in range(int(input())):
    i=-1
    j=int(input())
    print(sum(((i**w)/(2*w+1) for w in range(1,j) ))+1)
    
    
