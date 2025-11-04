"""
4. Implementar Radix Sort y ordenar las palabras de los archivos indicados.  
"""

def obtener_codigo(palabra, posicion):
    if posicion < len(palabra):
        return ord(palabra[posicion])
    return 0

def ordenar_por_posicion(palabras, posicion):
    total_codigos = 256
    conteo = [0] * (total_codigos + 1)

    for palabra in palabras:
        codigo = obtener_codigo(palabra, posicion)
        conteo[codigo] += 1

    acumulado = 0
    for i in range(total_codigos + 1):
        cantidad = conteo[i]
        conteo[i] = acumulado
        acumulado += cantidad

    resultado = [None] * len(palabras)

    for palabra in palabras:
        codigo = obtener_codigo(palabra, posicion)
        indice = conteo[codigo]
        resultado[indice] = palabra
        conteo[codigo] = indice + 1

    return resultado

def radix_sort_palabras(palabras):
    if not palabras:
        return []

    largo_maximo = max(len(p) for p in palabras)
    resultado = palabras[:]

    for posicion in range(largo_maximo - 1, -1, -1):
        resultado = ordenar_por_posicion(resultado, posicion)

    return resultado

def leer_palabras(ruta):
    archivo = open(ruta, "r", encoding="utf-8")

    palabras = []
    for linea in archivo:
        palabra = linea.strip()
        if palabra != "":
            palabras.append(palabra.lower())

    archivo.close()
    return palabras

def ejecutar():
    palabras = leer_palabras("EstructuraDeDatos\\ED-Practica-ed-2025-2c\\02.EstructurasLineales\\Ej4\\palabras.txt")
    palabras_ordenadas = radix_sort_palabras(palabras)
    print(palabras_ordenadas)

ejecutar()
