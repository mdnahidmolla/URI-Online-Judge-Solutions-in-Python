m = input().split()
a = int(m[0])
b = int(m[1])
c = int(m[2])
d = (a+b+abs(a-b))/2
d = (d+c+abs(d-c))/2
print("%d eh o maior" %d)


