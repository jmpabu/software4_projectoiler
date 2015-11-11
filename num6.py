a=0
b=0

for i in range(101):
    a+=(i**2)
    b+=i
b**=2

if a>b: print a-b
else: print b-a
