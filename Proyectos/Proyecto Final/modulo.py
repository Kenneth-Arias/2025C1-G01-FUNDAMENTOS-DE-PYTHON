import pandas as pd
import csv, os

def agregar_movimiento(lista_herramientas):
    while True:
        try: 
            herramienta = input('\nÍngrese el nombre del producto: ').upper()
            movimiento = input("¿Entrada o salida? (entrada/salida): ").strip().lower()
            if movimiento not in ['entrada', 'salida']:
                print("Movimiento inválido. Usa 'entrada' o 'salida'.")
                continue
            cantidad = int(input('Ingrese la cantidad: '))
            fecha = input('Íngrese la fecha de ingreso del producto (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del producto: '))
        except ValueError:  
            print('Entradas no validas, por favor intetenlo nuevamente!')
            continue
    
        memoria = {
            'herramienta' : herramienta,
            'movimiento' : movimiento,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
        }
         
        lista_herramientas.append(memoria)
        
        
        continuar = input('Desea ingresar otra herramienta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra herramienta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')
            
def guardar_movimientos(movimientos):
    if not movimientos:
        print('No hay movimientos que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append  'A'
            with open('movimientos.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','movimiento','cantidad','precio','fecha'])
                guardar.writerows(movimientos)        
        else: #Si no existe abro en modo escritura 'W'
            with open('movimientos.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['herramienta','movimiento','cantidad','precio','fecha'])
                guardar.writeheader()
                guardar.writerows(movimientos)
                
        movimientos = []
        print('\nDatos guardados exitosamente!')