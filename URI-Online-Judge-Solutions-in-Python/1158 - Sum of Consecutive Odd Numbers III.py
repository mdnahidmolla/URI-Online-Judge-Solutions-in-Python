def cria_lista(x, y):
    lista = []       
    while len(lista) != y:
        if impar(x) == True:
            lista.append(x)
        else:
            lista.append(x+1)
        x += 2
    return lista

impar = lambda a:a % 2 != 0

n = int(input())
for i in range(n):
    xy = input().split(); x, y = int(xy[0]), int(xy[1])
    print(sum(cria_lista(x, y)))