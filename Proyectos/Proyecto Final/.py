import json

with open('proyecto.json', encoding='utf-8') as archivo:
    inventario = json.load(archivo)
    
for producto in inventario:
    print(producto)