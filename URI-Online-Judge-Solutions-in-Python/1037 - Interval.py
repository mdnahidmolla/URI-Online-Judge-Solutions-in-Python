n = float(input())
if (n >= 0 and n <= 25.0000):
    print("Intervalo [0,25]")
elif (n >= 25.00001 and n <= 50.0000000):
    print("Intervalo (25,50]")
elif (n >= 50.00000001 and n <= 75.0000000):
    print("Intervalo (50,75]")
elif (n >= 75.00000001 and n <= 100.0000000):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")

