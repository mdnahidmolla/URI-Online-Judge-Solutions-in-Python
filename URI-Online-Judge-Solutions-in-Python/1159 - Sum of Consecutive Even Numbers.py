while 1:
    n = int(input())
    if(n==0):
         break
    sun = 0
    for i in range(5):
        if (n%2!=0):
            n+=1
        sun = sun + n
        n+=1
    print(sun)