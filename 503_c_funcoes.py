# -*- coding: utf-8 -*-
# Criando função que obtém o enésimo termo da sequência fibonacci
# O código está errado
# Você consegue corrigir?

def get_fibonacci(n):
  if n < 1:
    return 0
  ultimos_termos = [1, 1]
  for i in range(2, n):
    ultimos_termos = [ ultimos_termos[0] + ultimos_termos[1], ultimos_termos[1] ]
  return ultimos_termos[1]


while True:
  n = input("Qual termo da sequência fibonacci deseja obter? ")
  n = int(n)
  print(get_fibonacci(n))