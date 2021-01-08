m = 0
j = 0
for i in range(0,6,1):
    i = float(input())
    if i > 0:
        m += i
        j = j + 1
        all = m /j
print("%d valores positivos"%j)
print("%.1f" %all)