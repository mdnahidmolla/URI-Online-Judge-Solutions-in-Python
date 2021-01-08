t=int(input())

for i in range(t):
    n = int(input())
    sum = 0
    for x in range(1,n):
        if(n%x==0):
            sum+=x
    if(n == sum):
        print(sum,'eh perfeito')
    else:
        print(n,'nao eh perfeito')