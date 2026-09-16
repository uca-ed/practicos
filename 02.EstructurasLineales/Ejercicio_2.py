def representarCola(rutaArchivo):
    pila = [] 
    archivo = open(rutaArchivo, 'r')
    lineas = archivo.readlines()
    archivo.close()
    for linea in lineas:
        operacion = linea.strip().split(',')
        comando = operacion[0]
        
        if comando == 'PUSH':
            valor = operacion[1]
            pila.append(valor)
        elif comando == 'POP':
            if len(pila) > 0:
                pila.pop()  

    print("Pila final:", pila)