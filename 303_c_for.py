# -*- coding: utf-8 -*-
# Se listarmos os números menores que 10 e que são múltiplos de 3 e de 5, temos 3, 5, 6 e 9.
# A soma desse múltiplos é 23
# Descubra a soma de todos os múltiplos de 3 e de 5 e que são menores que 1000

limite = 1000

total = 0
for i in range(0, limite):
    if i % 3 == 0:
        total = total + i
    elif i % 5 == 0:
        total = total + i
print(total)