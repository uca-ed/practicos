def radix_sort(palabras):
    if not palabras:
        return palabras

    longitud = max(len(p) for p in palabras)

    for i in range(longitud - 1, -1, -1):
        grupos = {}
        for palabra in palabras:
            letra = palabra[i] if i < len(palabra) else " "  # si la palabra no llega a la posición i, usa un espacio
            if letra not in grupos:
                grupos[letra] = []
            grupos[letra].append(palabra)
        palabras = []
        for letra in sorted(grupos):  # ordena las letras alfabéticamente antes de concatenar
            palabras += grupos[letra]

    return palabras


with open("palabras.txt") as f:
    palabras = [linea.strip() for linea in f if linea.strip()]

print("Antes:", palabras)
print("Después:", radix_sort(palabras))
