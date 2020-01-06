## Agora vamos ler os dados do arquivo "pessoas.csv"
## E então escreve-lo em outro arquivo csv

import csv

def get_pessoas(filename):
    file_in = open(filename, "r")
    lines = file_in.readlines()
    pessoas = []
    for line in lines[1:]: # Pulando a primeira linha, que corresponde ao cabeçalho do CSV
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

def escrever_csv_basico(filename, pessoas):
    f_out = open(filename, 'r')
    f_out.write("idade,genero,peso,altura,imc")
    for pessoa in pessoas:
        dados = f"{pessoa['idade']},{pessoa['genero']},{pessoa['peso']},{pessoa['altura']},{pessoa['imc']}"
        f_out.write("\n")
        f_out.write(dados)


def escrever_csv_avancado(filename, pessoas):
    f_out = open(filename, 'w')
    keys = pessoas[0].keys()
    dict_writer = csv.DictWriter(f_out, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pessoas)

in_filename = "pessoas.csv"
out_filename_basico = "pessoas_basico.csv"
out_filename_avancado = "pessoas_avancado.csv"

pessoas = get_pessoas(in_filename)
escrever_csv_basico(out_filename_basico, pessoas)
escrever_csv_avancado(out_filename_avancado, pessoas)


