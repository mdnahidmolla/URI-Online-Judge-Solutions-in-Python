
for i in range(10):
    a = int(input())
    if (a==0) or (a<0):
        print("X[%d] = 1"%i)
    else:
        print("X[%d] = %d"%(i,a))