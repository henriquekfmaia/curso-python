import json

## Nesse exercício organizamos o arquivo medicare.json
## De modo que ele será organizado pelo código de id do provedor

json_file = open("medicare.json", "r")
file_text = json_file.read()
## É possível pegar um texto arquivo em formato json e transforma-lo em um dicionário
## Ou em uma lista de dicionários
medicare = json.loads(file_text)
# print(medicare)

medicare_by_provider = {}
for item in medicare:
    # print(item["provider_name"])
    medicare_by_provider[item["provider_id"]] = item


## E também é possível pegar um dicionário e transforma-lo em um json
new_json = json.dumps(medicare_by_provider, indent=4)
# O parâmetro "indent = 4" serve para formatar o json. Caso contrário todo texto ficará em apenas uma linha
file_out = open("medicare_by_provider.json", "w")
file_out.write(new_json)
