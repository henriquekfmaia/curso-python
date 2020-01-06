## Regras básicas de listas
## O código não precisa ser corrigido, pois é só uma demonstração

lista_teste = [ 1, 2, 3, 4, 5, 6 ]

print(f'Elementos da lista: {lista_teste}')
print(f'Tamanho da lista: {len(lista_teste)}')
## A lista começa a contar pelo 0
## Primeiro elemento = lista[0]
print(f'Primeiro elemento da lista: {lista_teste[0]}')
## Sexto elemento = lista[5]
print(f'Sexto elemento da lista: {lista_teste[5]}')
print(f'Ultimo elemento da lista: {lista_teste[-1]}')
print(f'Penultimo elemento da lista: {lista_teste[-2]}')
## Importante: Os "ranges" no python seguem a seguinte regra (a, b) significa (a, b(
## Ou seja: se falarmos dos números de a até b, ele na verdade irá de a até b-1
## range(0, 6) = 0, 1, 2, 3, 4, 5
print(f'Somente os três primeiros elementos da lista: {lista_teste[:3]}')
print(f'Eliminando os dois primeiros elementos da lista: {lista_teste[2:]}')
print(f'Três últimos elementos da lista: {lista_teste[-3:]}')
print(f'Eliminando os dois últimos elementos da lista: {lista_teste[:-2]}')
print(f'Somente do segundo ao quinto elementos da lista: {lista_teste[1:5]}')