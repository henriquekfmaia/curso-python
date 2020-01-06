import math

def calcular_variancia(amostra):
    soma = sum(amostra)
    media = soma/len(amostra)

    somatorio = 0
    for i in amostra:
        somatorio += math.pow((i - media), 2)

    variancia = somatorio/len(amostra)
    return variancia

def calcular_desvio_padrao(amostra):
    variancia = calcular_variancia(amostra)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao


amostra = [1, 2, 3, 4, 5, 6]
print(calcular_desvio_padrao(amostra))