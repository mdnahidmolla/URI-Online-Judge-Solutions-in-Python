x = int(input())
y = int(input())
s=0
if (x<y):
    x,y = x,y
    for i in range(x,y+1):
        if (i%13!=0):
            s+=i
    print(s)
if (x>y):
    x,y = x,y
    for i in range(y,x+1):
        if (i%13!=0):
            s+=i
    print(s)
