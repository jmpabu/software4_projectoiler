total=0
x=1
y=1
while y<=4000000:
    z=x+y
    if y%2==0:
        total+=y
    x=y
    y=z
print total
