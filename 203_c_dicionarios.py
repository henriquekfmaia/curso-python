## Outra estrutura muito importante são os dicionários
## Eles funcionam de forma semelhante a uma lista
## Entretanto, ao invés de organizar os elementos em índices 0, 1, 2, 3...
## Ele organiza em um sistema de chave -> valor

dicionario = {
    "nome": "Henrique Maia",
    "telefone": "(21) 98840-2580"
}

## Podemos consultar o dicionario da seguinte forma:
print(f"Nome: {dicionario['nome']}")
print(f"Telefone: {dicionario['telefone']}")

## Adicionar entradas ao dicionário
dicionario["email"] = "henrique.maia@decode.buzz"
dicionario["time de futebol"] = "Flamengo"
print(dicionario)

## Ou remover itens do dicionário
del dicionario["time de futebol"]
print(dicionario)