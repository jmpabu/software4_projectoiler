total=0
for x in range(100,1000):
    for y in range(100,1000):
        p="%s"%(x*y)
        pp=p[::-1]
        if p==pp:
            if total<x*y:
                total=x*y
print total
