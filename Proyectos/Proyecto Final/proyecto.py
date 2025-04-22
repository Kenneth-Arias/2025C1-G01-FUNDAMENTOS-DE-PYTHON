#Proyecto de Kenneth Arias Solís 
#Sistema de organizacion de inventario

#importaciones
import os
import pandas as pd

from modulo import ingresar_herramientas


#Funciones y variables 
def pause():
    input("Presione cualquier tecla para continuar...")
    

def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system('cls' if os.name == 'nt' else 'clear')
    

#Menú principal
print("\nBienvenido al Sistema de organizacion de Inventario")

while(True):
    print('\n-------- MENÚ PRINCIPAL --------')
    print('1. Ingresar Herramientas')
    print('2. Venta de Herramientas')
    print('3. Guardar datos en un archivo CSV')
    print('4. Analizar los datos')
    print('5. Salir')
    opcion = input('Ingrese una opción: ')
    
    if opcion == "1":
        ingresar_herramientas()
        pause()
        
    elif opcion == "2":
        pause()
        
    elif opcion == "3":
        pause()
        
    elif opcion == "4":
        pause()
        
    elif opcion == "5":
        print('Muchas gracias por usar el programa!!')
        pause()
        break
    
    else:
        print('Opcion no valida, vuelva a intenterlo')
        pause()