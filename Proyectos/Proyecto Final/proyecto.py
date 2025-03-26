import json

with open(r"C:\Users\Admin\OneDrive\Documents\GitHub\2025C1-G01-FUNDAMENTOS-DE-PYTHON\Proyectos\Proyecto Final\proyecto.json") as archivo:
    inventario = json.load(archivo)

for producto in inventario:
    nombre = producto[0]
    cantidad = producto[1]
    print(f"Producto: {nombre}, Cantidad: {cantidad}")

print("Agregar articulo: ")
if input("Desea agregar o modificar el inventario? SI o NO? ").upper == "SI":
    
    productoN = input("Ingrese el nombre del producto: ")
    cantidadN = int(input("Ingrese la cantidad: "))
    
    for producto in inventario:
        if producto[0].lower() == productoN.lower():
            producto[1] += cantidadN
            break

for cantidad in inventario:
        if cantidad >= 50:
            (f"OVERSTOCK: {producto} tiene {cantidad} unidades.")
        elif cantidad < 10:
            (f"STOCK BAJO: {producto} tiene solo {cantidad} unidades.")
        else:
            print(" No hay alertas de inventario.")
        
        
for producto in inventario:
    nombre = producto[0]
    cantidad = producto[1]
    print(f"Producto: {nombre}, Cantidad: {cantidad}")

