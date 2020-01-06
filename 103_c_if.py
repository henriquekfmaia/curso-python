# -*- coding: utf-8 -*-
# Verificando a letra digitada é uma vogal
# Você consegue encontrar o que tem de errado?

a = input('Digite uma letra')

vogais = [ "a", "e", "i", "o", "u" ]

if len(a) != 1:
  print("Por favor, digite apenas uma letra")
elif a.lower() not in vogais:
    print("A sua letra é uma vogal")
else:
    print("A sua letra não é uma vogal")