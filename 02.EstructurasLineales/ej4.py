def radix_sort_palabras(palabras):
    if not palabras:
        return palabras

    # Encontrar la longitud máxima de las palabras
    max_len = max(len(p) for p in palabras)

    # Rellenar palabras más cortas con espacios al final
    palabras_pad = [p.ljust(max_len) for p in palabras]

    # Ordenar de derecha a izquierda por cada caracter
    for pos in range(max_len - 1, -1, -1):
        # Crear 27 cestas: 1 para espacio + 26 para letras a-z
        cestas = [[] for _ in range(27)]

        for palabra in palabras_pad:
            char = palabra[pos].lower()
            if char == ' ':
                indice = 0
            else:
                indice = ord(char) - ord('a') + 1
            cestas[indice].append(palabra)

        # Reunir todas las cestas
        palabras_pad = []
        for cesta in cestas:
            palabras_pad.extend(cesta)

    # Quitar el relleno de espacios
    return [p.strip() for p in palabras_pad]


def main():
    try:
        with open("frutas_ej4.txt", "r") as archivo:
            palabras = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print("Error: no se encontró el archivo 'frutas_ej4.txt'")
        return

    print("Palabras originales:")
    print(palabras)

    ordenadas = radix_sort_palabras(palabras)

    print("\nPalabras ordenadas con Radix Sort:")
    print(ordenadas)


if __name__ == "__main__":
    main()
