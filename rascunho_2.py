import random
import csv

def gerar_pessoa():
    idade = random.randint(20, 30)
    genero_masculino = random.randint(0, 1)
    # genero_masculino = random.choice([True, False])
    if genero_masculino:
        genero = "masculino"
        peso = random.randint(70, 110)
        altura = random.randint(160, 210)/100
    else:
        genero = "feminino"
        peso = random.randint(50, 90)
        altura = random.randint(150, 190)/100
    imc = peso/(altura*altura)
    pessoa = {
        "idade": idade,
        "genero": genero,
        "peso": peso,
        "altura": altura,
        "imc": imc
    }
    return pessoa

filename = "pessoas.csv"

pessoas = []
for i in range(0, 10000):
    pessoas.append(gerar_pessoa())


f_out = open(filename, 'w')
keys = pessoas[0].keys()
dict_writer = csv.DictWriter(f_out, keys)
dict_writer.writeheader()
dict_writer.writerows(pessoas)