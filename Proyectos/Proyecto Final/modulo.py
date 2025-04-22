import pandas as pd
import csv, os

def ingresar_herramientas(lista_herramientas):
    while True:
        try: 
            herramienta = input ('Íngrese el nombre del producto: ').upper()
            cantidad = int (input('Ingrese la cantidad de productos vendidos: '))
            fecha = input('Íngrese la fecha de ingreso del producto (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del producto: '))
        except ValueError:
            print('Entradas no validas, por favor intetenlo nuevamente!')
            continue
    
        herramienta = {
            'herramienta' : herramienta,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
        }
        
        lista_herramientas.append(herramienta)
        
        
        continuar = input('Desea ingresar otra herramienta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra herramienta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')