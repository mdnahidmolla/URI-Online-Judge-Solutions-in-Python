n = str(input())
m = n.split(" ")
A = int(m[0])
B = int(m[1])
if (A%B==0) or (B%A==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")