l = []
m = 0
p = 0
t = int(input())
for n in range(1,(t+1)):
    l.append(int(input()))

for n in l:
    if 10<=n and n<=20:
        m = m + 1

    else:
        p = p + 1

print(m,"in")
print(p,"out")