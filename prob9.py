import math
for i in range(200,1000):
    for j in range(200,1000):
        for k in range(200,1000):
            
            if (i**2)+(j**2) == (k**2) and i+j+k == 1000:
                print(i*j*k)
                break
