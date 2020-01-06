
## Lê os dados de um arquivo csv
## Consegue obter uma lista de alturas e de IMC?
## Consegue filtrar os dados obtidos por gênero, ou por alguma outra característica da pessoa?

def get_pessoas(filename):
    file_in = open(filename, "r")
    lines = file_in.readlines()
    pessoas = []
    for line in lines:
        line = line.replace("\n", "") ## Removendo a quebra de linha do final de cada linha
        dados = line.split(",")
        pessoa = {
            "idade": dados[0],
            "genero": dados[1],
            "peso": dados[2],
            "altura": dados[3],
            "imc": dados[4]
        }
        pessoas.append(pessoa)
    return pessoas

def get_pesos(filename):
    file_in = open(filename, "r")
    lines = file_in.readlines()
    pesos = []
    for line in lines:
        line = line.replace("\n", "") ## Removendo a quebra de linha do final de cada linha
        dados = line.split(",")
        peso = dados[2]
        pesos.append(peso)
    return pesos

filename = "pessoas.csv"
pessoas = get_pessoas(filename)
pesos = get_pesos(filename)