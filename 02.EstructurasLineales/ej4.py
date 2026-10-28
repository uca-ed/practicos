def indice_caracter(palabra, posicion):
    # 0 se reserva para palabras que ya no tienen carácter en esta posición.
    if posicion >= len(palabra):
        return 0

    caracter = palabra[posicion].lower()

    # Este TP usa palabras sin tildes y letras a-z.
    if "a" <= caracter <= "z":
        return ord(caracter) - ord("a") + 1

    raise ValueError("Las palabras deben contener solamente letras a-z.")


def radix_sort_palabras(palabras):
    if len(palabras) == 0:
        return []

    resultado = palabras[:]
    max_len = max(len(palabra) for palabra in resultado)

    # LSD: se procesa desde el último carácter hacia el primero.
    for posicion in range(max_len - 1, -1, -1):
        colas = [[] for _ in range(27)]

        for palabra in resultado:
            indice = indice_caracter(palabra, posicion)
            colas[indice].append(palabra)

        resultado = []
        for cola in colas:
            resultado.extend(cola)

    return resultado


with open("palabras.txt", "r", encoding="utf-8") as archivo:
    palabras = [linea.strip() for linea in archivo if linea.strip()]

ordenadas = radix_sort_palabras(palabras)

print("Palabras ordenadas:")
for palabra in ordenadas:
    print(palabra)
