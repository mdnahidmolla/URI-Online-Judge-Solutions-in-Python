n = float(input())
if n>0:
    if n<=400:
        x = n*15/100
        print("Novo salario: %.2f"%(n+x))
        print("Reajuste ganho: %.2f" %x)
        print("Em percentual: 15 %")

if n>=400.01:
    if n<=800.00:
        x = n*12/100
        print("Novo salario: %.2f"%(n+x))
        print("Reajuste ganho: %.2f" %x)
        print("Em percentual: 12 %")

if n>=800.01:
    if n<=1200.00:
        x = n*10/100
        print("Novo salario: %.2f"%(n+x))
        print("Reajuste ganho: %.2f" %x)
        print("Em percentual: 10 %")

if n>=1200.01:
    if n<=2000.00:
        x = n*7/100
        print("Novo salario: %.2f"%(n+x))
        print("Reajuste ganho: %.2f" %x)
        print("Em percentual: 7 %")
if n>2000.00:
    x=n*4/100
    print("Novo salario: %.2f" % (n + x))
    print("Reajuste ganho: %.2f" % x)
    print("Em percentual: 4 %")
