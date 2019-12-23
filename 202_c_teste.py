# Diferenciando se um número é par ou ímpar
# O código está errado
# Você consegue corrigir?

a = input('Digite um número: ')

if not a.isdigit():
    print("Eu disse um número!")
elif (int(a) % 2) != 0:
    print("Seu número é par")
elif (int(a) % 2) == 0:
    print("Seu número é ímpar")
else:
    print("Eu nunca vou chegar aqui")