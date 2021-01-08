t=int(input())
a,b,c,cont=0,0,0,0
for i in range(1,(t+1)):
    l=input().split()
    n=int(l[0])
    d=(l[1])
    cont+=n
    if (d=='C'):
        a=a+n
    elif(d=='R'):
        b=b+n
    elif(d=='S'):
        c=c+n

print('Total: %d cobaias' %cont)
print('Total de coelhos: %d' %a)
print('Total de ratos: %d' %b)
print('Total de sapos: %d' %c)
print('Percentual de coelhos: %.2f' %float(((100*a)/cont)),'%')
print('Percentual de ratos: %.2f' %float(((100*b)/cont)),'%')
print('Percentual de sapos: %.2f' %float(((100*c)/cont)),'%')
