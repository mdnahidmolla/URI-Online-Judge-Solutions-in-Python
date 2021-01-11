even = 0
odd = 0
pos = 0
neg = 0
for i in range(5):
    n = int(input())
    if(n%2 == 0):
        even = even+1
    else:
        odd = odd+1
    if(n > 0):
        pos = pos+1
    elif(n < 0):
        neg = neg+1
print("%d valor(es) par(es)"%even)
print("%d valor(es) impar(es)"%odd)
print("%d valor(es) positivo(s)"%pos)
print("%d valor(es) negativo(s)"%neg)


