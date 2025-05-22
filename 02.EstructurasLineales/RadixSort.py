#Implementar Radix Sort y ordenar las palabras de los archivos indicados.

import json

def obtener_alfabeto_por_nombre(alfabetos,nombre):
    #Esta funcion reccore todos los alfabetos hasta encontrar el que necesito
    for alfabeto in alfabetos:
        if alfabeto['nombre'] == nombre:
            return alfabeto['caracteres']
    return None #Si no lo encuento retorno null para evvitar error

def largo_maximo_palabras(palabras):
    max_longitud = 0
    for palabra in palabras:
        if len(palabra) > max_longitud:
            max_longitud = len(palabra)
    return max_longitud

def obtener_caracter_por_indice(palabra, posicion, alfabeto):
    longitud_palabra = len(palabra)
    if longitud_palabra - 1 - posicion < 0:
        return -1  # No hay carácter en esa posición
    caracter = palabra[longitud_palabra - 1 - posicion]
    return indice_en_alfabeto(caracter, alfabeto) #Checo si esta y donde esta esa letra en el alfabeto

def indice_en_alfabeto(caracter, alfabeto):
    for i in range(len(alfabeto)):
        if alfabeto[i] == caracter:
            return i #Retorno donde esta esa letra en el alfabeto
    return -1  # Si el carácter no está en el alfabeto

def ordenamiento_por_caracter(palabras,posicion,alfabeto):
    palabras_ordenadas = [''] * len(palabras) #Una lista del tamaño de las palabras donde las voy a guardar ya ordenadas
    count = [0] * len(alfabeto) # almacena cuantas veces aparece una letra del abecedario en las palabras, despues ayuda
    #a ordenar mas facil pues si hay 2 a y 2c quiere decir que las dos palabras con a van primero luego van las 2 de c
    #(ya que hay  en b) y asi
    
    # Contar las veces que aparece cada letra del abecedario en cada palabra
    for palabra in palabras:
        char_index = obtener_caracter_por_indice(palabra, posicion, alfabeto)
        if char_index != -1:
            count[char_index] += 1 #Sumo una cada vez que aparece, el char_index es la posicion de la letra en cuestion
            #dentro del abecedario

    # Cambiar count[i] para que contenga la posición real en output
    
    #Explicacion:
    """
    Después de contar cuántas veces aparece cada carácter en la posición actual ,la lista count contiene la cantidad
    de veces que aparece  cada carácter. Sin embargo, para poder ordenar las palabras correctamente necesitamos
    convertir estas cantidades en posiciones reales donde cada carácter debe ir en la lista ordenada.

    """
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir el array de salida
    for i in range(len(palabras) - 1, -1, -1): #  itera sobre la lista palabras desde el último elemento hasta el primero. 
        palabra = palabras[i]
        char_index = obtener_caracter_por_indice(palabra, posicion, alfabeto)
        if char_index != -1:
            palabras_ordenadas[count[char_index] - 1] = palabra
            count[char_index] -= 1

    return palabras_ordenadas

def radix_sort(alfabetos,lenguaje,palabras):
    """Verificacion 
    for alfabeto in alfabetos:
        print(f"Nombre: {alfabeto['nombre']}, Caracteres: {', '.join(alfabeto['caracteres'])}")
    print(f"Nombre del lenguaje: {lenguaje['nombre']}, Orden: {', '.join(lenguaje['orden'])}")
    for palabra in palabras:
        print(palabra)
    """
    
    #Ahora voy a hacer lo siguiente, como yo supongo que una palabra esta formada por mas de un tipo
    #de alfabeto, necesito recorrer por cada uno de los alfabetos en orden evaluando y ordenando las palabras
    
    for alfabeto_actual_nombre in lenguaje['orden']:#Reccoro el orden de los alfabetos que me dice el lenguaje
        alfabeto_actual = obtener_alfabeto_por_nombre(alfabetos,alfabeto_actual_nombre) #obtengo el alfabeto que necesito en esta iteracion
        if alfabeto_actual is not None: #Para evitar errores me aseguro obtener un alfabeto
            largo_maximo = largo_maximo_palabras(palabras)# Necesito saber esto para saber cuantos caracteres en total tengo que avanzar en cada palabra
            for i in range(largo_maximo):#Ahora recorro todos los caracteres por cada palabra
                palabras_ordenadas = ordenamiento_por_caracter(palabras,i,alfabeto_actual)#Ordeno palabras por caracter
    return palabras_ordenadas
    

def main():
    
    #CUAL DE LOS DOS VOY A ORDENAS 1=a1 0=1a
    elecion=1
    
    
    #Primero cargo los archivos
    
    # Leer el archivo JSON
    with open('alfabetos.json', 'r') as archivo:
        data = json.load(archivo)

    # Acceder a los alfabetos
    alfabetos = data['alfabetos']
    
    """#Para verificar 
    # Imprimir los nombres y caracteres de cada alfabeto
    for alfabeto in alfabetos:
        print(f"Nombre: {alfabeto['nombre']}, Caracteres: {', '.join(alfabeto['caracteres'])}")
    """
    #==========================================================================================
    #Ahora los lenguajes: 
    with open('lenguaje.json', 'r') as archivo:
        data = json.load(archivo)
        
    lenguajes = data['lenguaje']
    
    """
    for lenguaje in lenguajes:
        print(f"Nombre del lenguaje: {lenguaje['nombre']}, Orden: {', '.join(lenguaje['orden'])}")
    """
    #==============================================================================================
    #Ahora las palabras: 
    with open('palabras.json', 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)


    palabras = data['palabras'][elecion]['palabras']
    """
    for palabra in palabras:
        print(palabra)
    """
    print("Palabras no ordenadas: ")
    for palabra in palabras:
        print(palabra)
        
    palabras_ordenadas = radix_sort(alfabetos,lenguajes[elecion],palabras)
    
    print("Palabras  ordenadas: ")
    for palabra in palabras_ordenadas:
        print(palabra)
        
main()
