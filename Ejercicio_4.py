#asigno a cada caracter de un alfabeto un número entero
def orden(alfabeto):
    orden = {}
    i = 0
    for letra in alfabeto:
        orden[letra] = i
        i += 1
    return orden

# Algoritmo radix sort con orden personalizado por posición
def radix_sort_personalizado(palabras, alfabetos_por_posicion):
    pos = len(alfabetos_por_posicion) - 1
    while pos >= 0:
        alf = alfabetos_por_posicion[pos]
        orden_alf = orden(alf)
        for i in range(len(palabras)):
            for j in range(i + 1, len(palabras)):
                if orden_alf[palabras[i][pos]] > orden_alf[palabras[j][pos]]:
                    palabras[i], palabras[j] = palabras[j], palabras[i]
        pos -= 1
    return palabras


def main():
    sigma_1 = ['A', 'B', 'C']
    sigma_2 = ['1', '3', '2', '4']
    
    pal = ["C21", "B33", "A11", "A21"]
    alfpos = [sigma_1, sigma_2, sigma_2]

    print("Palabras originales:", pal)
    resultado = radix_sort_personalizado(pal, alfpos)
    print("Palabras ordenadas:", resultado)

# Llamada al main
if __name__ == "__main__":
    main()
