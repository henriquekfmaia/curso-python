import csv

def escrever_csv_avancado(filename, pessoas):
    f_out = open(filename, 'w')
    keys = pessoas[0].keys()
    dict_writer = csv.DictWriter(f_out, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pessoas)

out_filename_avancado = "pessoas_avancado.csv"

escrever_csv_avancado(out_filename_avancado, pessoas)