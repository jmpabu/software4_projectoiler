x=21
while True:
    for i in range(2,20):
        if x%i>0:
            break
    else:
        print x
        break
    x+=1
