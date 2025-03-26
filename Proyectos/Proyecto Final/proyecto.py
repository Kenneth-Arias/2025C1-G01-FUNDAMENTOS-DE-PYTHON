import json

with open('proyecto.json') as archivo:
    inventario = json.load(archivo)
    print('Datos de los pacientes cargados con éxito!\n')
    
for producto in inventario:
    print(producto)