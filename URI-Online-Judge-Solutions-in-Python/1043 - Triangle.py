#URI Online Judge | 1043 Triângulo
x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
if(a < b + c) and (b < a + c) and (c < a + b):
  per = a + b + c
  print('Perimetro = %.1f' %per)
else:
  ar = ((a + b) * c) / 2
  print('Area = %.1f' %ar)