filename = "output.txt"
conteudo = input("Digite o texto que será escrito no arquivo:\n")
file_out = open(filename, "w") # O parâmetro "w" significa "write", indicando que o arquivo somente será escrito
file_out.write(conteudo)