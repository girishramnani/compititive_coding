mem =dict()

def ans(x,y):
    import pdb
    pdb.set_trace()
    
    if x<1 or y <1:
        return 0
    if x==y:
        return 0
    elif x>y:
        return an
    
    an =1+ min(ans(x*2,y),ans(x-1,y))
    mem[x] = an
    return an
        
t =4
w=6
print(ans(4,6))
