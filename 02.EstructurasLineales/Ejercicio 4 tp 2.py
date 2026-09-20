def radix_sort(palabras):

    archivo = open("palabras.txt", "r")

    palabras = []

    for linea in archivo:
        palabras.append(linea.strip())

    archivo.close()
    mayor = 0

    for palabra in palabras:
        if len(palabra) > mayor:
            mayor = len(palabra)

    for posicion in range(mayor - 1, -1, -1):

        grupos = {}

        for palabra in palabras:

            if posicion < len(palabra):
                letra = palabra[posicion]
            else:
                letra = ""

            if letra not in grupos:
                grupos[letra] = []

            grupos[letra].append(palabra)

        palabras = []

        for grupo in grupos:
            for palabra in grupos[grupo]:
                palabras.append(palabra)

    return palabras


archivo = open("palabras.txt", "r")

palabras = []

for linea in archivo:
    palabras.append(linea.strip())

archivo.close()

palabras = radix_sort(palabras)

print(palabras)