filename = "zen.txt"
file_in = open(filename, "r") # O parâmetro "r" significa "read", indicando que o arquivo somente será lido
text = file_in.read()
# file_in = open(filename, "r")
lines = file_in.readlines()
print("Texto completo:")
print(text)
print("-------------------------------------------------")
print(lines)