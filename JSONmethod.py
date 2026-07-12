import json
from pprint import pprint
dizionario = { "name": "John", "age": 30, "city": "New York", "country": "USA" }

json_dizionario = json.dumps(dizionario)
print(type(json_dizionario))
print(json_dizionario)


dati_web = '{"modello": "Llama-3", "temperatura": 0.7, "offline": true}'
json_dati_web = json.loads(dati_web)
print(json_dati_web)
print(type(json_dati_web))


json_dati_web["temperatura"] = 0.2
print(json_dati_web)

json_dati_web_json = json.dumps(json_dati_web)
print(type(json_dati_web_json))
print(json_dati_web_json)

dati_web2 = {"modello": "Llama-3", "temperatura": 0.7, "offline": True}
json_dati_web2 = json.dumps(dati_web2)
print(type(json_dati_web2))
print(json_dati_web2)
pprint(json.loads(json_dati_web2), indent=4, sort_dicts=True)

