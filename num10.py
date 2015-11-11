import math

i=2
total=0

while True:
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            break
    else:
        if i<=2000000:
            total+=i
        else:
            break
    i+=1

print total
