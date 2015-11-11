import math

def num9(x):
    for i in range(1,x):
        for j in range(i,x):
            k = int(math.sqrt(i**2 + j**2))
            if k**2 == i**2 + j**2:
                if i+j+k==x:
                    print i*j*k
                    return

num9(1000)
