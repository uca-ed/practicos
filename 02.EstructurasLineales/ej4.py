alfabeto = "abcdefghijklmnopqrstuvwxyz"
Q = []

archivo = open("palabras.txt", "r")
for linea in archivo:
    palabra = linea.strip()
    if palabra != "":
        Q.append(palabra)
archivo.close()

if len(Q) > 0:
    longitud = len(Q[0])

    # desde la ultima posicion hasta la primera
    for j in range(longitud - 1, -1, -1):
        colas = []
        for i in range(len(alfabeto)):
            colas.append([])

        while len(Q) > 0:
            palabra = Q.pop(0)
            simbolo = palabra[j]
            numero_cola = alfabeto.index(simbolo)
            colas[numero_cola].append(palabra)

        # concatenamos las colas en el orden del alfabeto
        for i in range(len(alfabeto)):
            while len(colas[i]) > 0:
                palabra = colas[i].pop(0)
                Q.append(palabra)

print("Palabras ordenadas:")
for palabra in Q:
    print(palabra)
