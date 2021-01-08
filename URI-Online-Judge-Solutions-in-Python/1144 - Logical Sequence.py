n = int(input())
i = 1
a = 1
b = 1
c = 1
while n>=i:
    print("%d %d %d" %(a,b**2,c**3))
    print("%d %d %d" % (a, b*b+1, c**3+1))
    i+=1
    a+=1
    b+=1
    c+=1
