def representarCola(rutaArchivo):
    cola = [] 
    archivo = open(rutaArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        operacion = linea.strip().split(',') #Sacamos el /n del final y dividimos la linea en la accion y el valor#
        comando = operacion[0]

        if comando == 'ENQUEUE':  #Vemos cual es la palabra de accionamiento y interactuamos como corresponda sobre la cola#
            valor = operacion[1]
            cola.append(valor)
        elif comando == 'DEQUEUE':
            if len(cola) > 0:
                cola.pop(0)
                
    print("Cola final:", cola)