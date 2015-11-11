num = 600851475143
x = num
while x>1:
    if num%(-x)==0:
        y=2
        while y*y<=x:
            if x%y==0:
                break
            y+=1
        else:
            print x
            break
    x-=1
