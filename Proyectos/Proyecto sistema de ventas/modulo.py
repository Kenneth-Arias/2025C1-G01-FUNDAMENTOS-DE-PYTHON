def ingresar_ventas():
    while True:
        try:
            curso = input ('Ingresar el nombre del curso: ').upper()
            cantidad = int('Ingrese la cantidad de cursos vendidos:')
            fecha = input('Ingrese la fecha de la venta (AAAA-MM-DD):')
            precio = float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente').upper()
        except ValueError:
            print('Entradas no valida, por favor intentelo nuevamente')
            continue
        
        venta = {
            'curso': curso,
            'cantidad': cantidad,
            'precio': precio,
            'fecha': fecha,
            'cliente': cliente
        }
        lista_ventas.append(venta)
        
        #Ingresar la venta
        continuar = input('Desea ingresar otra venta s/n : ')
        if continuar == 's':
            print('\n ---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else:
            print('Opcion no valida')
    
            
    