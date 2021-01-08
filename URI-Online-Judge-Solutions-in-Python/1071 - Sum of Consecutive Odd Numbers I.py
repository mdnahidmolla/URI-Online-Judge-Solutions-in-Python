n=int(input())
m=int(input())
s=0
for i in range(m+1,n):
    if (i%2!=0):
        s+=i
print(s)