n = int(input())
li = [int(x) for x in input().split()]
zeros = [0 for _ in range(n)]


def subsum(li):
    s = 0
    m_s = float("-inf")
    for i in range(len(li)):
        s+=li[i]
        if s < 0:
            s = 0
        if s > m_s:
            m_s = s


    return m_s


if all(li):
    print(n-1)
else:    
    for i in range(len(li)):
        
        if li[i] == 1:
            zeros[i] = -1
        else:
            zeros[i] = 1

        
    
    print(len(list(filter(lambda x: x == 1, li)))+ subsum(zeros))
