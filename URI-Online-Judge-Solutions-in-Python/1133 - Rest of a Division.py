# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
#URI Online Judge | 1133 Resto da Divisão
a = int(input())
b = int(input())
if(a > b):
  a, b = b, a
for i in range(a + 1, b):
  if(i % 5 == 2) or (i % 5 == 3):
    print(i)