
archivos = ["archivo1.txt", "archivo2.txt"] 

palabras = []

for nombre_archivo in archivos:
    f = open(nombre_archivo, "r", encoding="utf-8")
    contenido = f.read()
    f.close()
    for palabra in contenido.split():
        # paso todo a minusculas
        palabras.append(palabra.lower())

print("Cantidad de palabras leidas:", len(palabras))

max_largo = 0
for palabra in palabras:
    if len(palabra) > max_largo:
        max_largo = len(palabra)

BASE = 27  

for posicion in range(max_largo - 1, -1, -1):

    conteo = [0] * (BASE + 1)
    for palabra in palabras:
        if posicion < len(palabra):
            c = palabra[posicion]
            indice_digito = ord(c) - ord('a') + 1
        else:
            indice_digito = 0  
        conteo[indice_digito] += 1

    # acumulo conteos para saber las posiciones finales
    for i in range(1, BASE + 1):
        conteo[i] += conteo[i - 1]

    salida = [None] * len(palabras)
    for i in range(len(palabras) - 1, -1, -1):
        palabra = palabras[i]
        if posicion < len(palabra):
            c = palabra[posicion]
            indice_digito = ord(c) - ord('a') + 1
        else:
            indice_digito = 0
        conteo[indice_digito] -= 1
        salida[conteo[indice_digito]] = palabra

    palabras = salida

print("\nPalabras ordenadas:")
for palabra in palabras:
    print(palabra)
