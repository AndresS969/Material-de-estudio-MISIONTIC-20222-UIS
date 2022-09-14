import json 

lista = [12,11,24,30,60,80,90,10,5,8]
with open("lista.json", "w") as f:
    json.dump(lista, f)

#para cargar json:
with open("lista.json") as f:
    print(json.load(f))