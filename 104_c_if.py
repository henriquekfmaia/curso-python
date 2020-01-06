# -*- coding: utf-8 -*-
# O código abaixo deve dizer se um número é primo ou não
# O código está incompleto
# Como podemos torna-lo funcional?

n = input("Digite um número: ")
numero = int(n)

es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break

if es_primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')