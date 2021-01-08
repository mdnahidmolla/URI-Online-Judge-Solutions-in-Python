x,y = map(int,input().split(" "))
if x == 1:
    Total=4*y
elif x == 2:
    Total=4.5*y
elif x == 3:
    Total=5*y
elif x == 4:
    Total=2*y
elif x == 5:
    Total=1.5*y
print("Total: R$ {:0.2f}" .format(Total))
