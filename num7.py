import math

count = 0
i=2

while True:
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            break
    else:
        count+=1
        if count==10001:
            print i
            break
    i+=1
