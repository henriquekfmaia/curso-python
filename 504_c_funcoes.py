# -*- coding: utf-8 -*-
# Criando função que obtém o enésimo termo da sequência fibonacci
# Dessa vez vamos usar o conceito de recursividade (quando uma função chama ela mesma)
# O código está errado
# Você consegue corrigir?

def get_fibonacci(n):
  if n < 1:
    return 0
  elif n < 3:
    return 1
  else:
    fib_menos_1 = get_fibonacci(n-1)
    fib_menos_2 = get_fibonacci(n-2)
    return fib_menos_1 + fib_menos_2

while True:
  n = input("Qual termo da sequência fibonacci deseja obter? ")
  n = int(n)
  print(get_fibonacci(n))