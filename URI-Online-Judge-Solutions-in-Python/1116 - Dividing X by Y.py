t = int(input())
for i in range(1,t+1):
    a,b = map(int,input().split())
    if b == 0:
        print("divisao impossivel")
    elif(b != 0):
        divi = a/b
        print(divi)
