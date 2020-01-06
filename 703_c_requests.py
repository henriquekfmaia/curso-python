## A biblioteca requests é usada para fazer chamadas HTTP
## Normalmente usada para acessar dados de API

import requests

url = "https://data.cms.gov/resource/97k6-zzx3.json"

## Normalmente as chamadas HTTP se enquadram em quatro tipos principais
## GET (leitura), POST (criação de um registro), PUT (atualização de um registro), DELETE (apagar um registro)
## Dentre esses, os mais usados são GET e POST
## Existem ainda outros métodos, mas são menos utilizados
response = requests.get(url)
result = response.text
# print(result)

## Exercício 1: salvar o a resposta dessa chamada em um arquivo
## Exercício 2: salvar o a resposta dessa chamada em um arquivo,
## mas dessa vez organizado pelo nomme do provedor do medicare