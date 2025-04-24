"""
Autor: Kenneth Arias Solís
Fecha: 2025-4-16
Version: 0.1
Sistema de Gestion de Ventas nos permita.
"""

import os    
from modulo import ingresar_ventas, guardar_ventas, analisis_ventas

def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPresione Enter para continuar...')

#Menu Principal
def menu():
    
    #Variables del sistena
    ventas = []
    
    while True:
        print('\n---- MENÚ PRINCIPAL ----')
        print('1. Ingresar ventas de cursos UMCA')
        print('2. Guardar datos en un archivo CSV')
        print('3. Analizar los datos')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == "1":
            print('\n ---- Ingresar ventas de cursos UMCA ----')
            ingresar_ventas(ventas)
            print(*ventas)
            pausar()
        elif opcion == "2":
            print('\n ---- Guardar datos en un archivo CSV ----')
            guardar_ventas(ventas)
            pausar()
        elif opcion == '3':
            limpiar_pantalla()
            print('\n ---- Analisis de Ventas ----')
            analisis_ventas()
            pausar()
        elif opcion == "4":
            print('\nGracias por usar el sistema. Hasta pronto')
            pausar()
            break #Cierre
        else:
            print('Opción no válida. Intente nuevamente una opcion!')
            pausar()
            
            
#Ejecucion del sistema si solo si el archivo es el main
if __name__ == '__main__':
    print('Bienvenido la sistema de gestion de ventas')
    pausar()
    menu()