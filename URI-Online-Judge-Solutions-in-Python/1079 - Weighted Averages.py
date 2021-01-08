t = int(input())
for n in range(1,(t+1)):
    a, b, c = map(float, input().split())
    total = (a * 2) + (b * 3) + (c * 5)
    m = total / 10
    print("%.1f"%m)


