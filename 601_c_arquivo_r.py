filename = "zen.txt"
file_in = open(filename, "r") # O parâmetro "r" significa "read", indicando que o arquivo somente será lido
## O comando read() retorna todo o texto do arquivo
text = file_in.read()
# file_in = open(filename, "r")
## O comando readlines() retorna uma lista com cada linha do texto que está dentro do arquivo
lines = file_in.readlines()
print("Texto completo:")
print(text)
print("-------------------------------------------------")
print(lines)