#Proyecto de Kenneth Arias Solís 
#Sistema de organizacion de inventario

#importaciones
import os
import pandas as pd

from modulo import agregar_movimiento, guardar_movimientos


#Funciones
def pause():
    input("Presione ENTER para continuar...")
    

def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system('cls' if os.name == 'nt' else 'clear')
    

#Menú principal
def menu():
    print("\nBienvenido al Sistema de organizacion de Inventario")
    
    #Variables del sistema
    movimientos = []
    
    while(True):
        print('\n--- Sistema de Inventario de Ferretería ---')
        print('1. Agregar movimientos a la memoria')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar los datos')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == "1":
            agregar_movimiento(movimientos)
            print(*movimientos)
            pause()

        elif opcion == "2":
            guardar_movimientos(movimientos)
            pause()

        elif opcion == "3":
            pause()

        elif opcion == "4":
            print('Muchas gracias por usar el programa!!')
            pause()
            break
        
        else:
            print('Opcion no valida, vuelva a intenterlo')
            pause()
            
            
if __name__ == '__proyecto__':
    print('Bienvenido la sistema de gestion de ventas')
    pause()
    menu()