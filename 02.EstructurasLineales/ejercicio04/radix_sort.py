

def radixSort(words, alfabet):
    
    p = len(alfabet)

    for j in range(1, p+1):
        r = len(alfabet[j-1])
        colas = [ [] for _ in range(r)]

        for palabra in words:
            simbolo = palabra[-j]
            indice = alfabet[j-1].index(simbolo)
            colas[indice].append(palabra)

        palabras =[]
        for cola in colas:
            for elem in cola:
                palabras.append(elem)

        words = palabras

    return palabras

        
def main():
    alfabetos = []

    archivo = open('alfabeto.txt')
    for linea in archivo:
        alfabetos.append(linea.strip().split(','))
    archivo.close()

    palabras = []
    archivo2 = open('palabras.txt')
    for linea in archivo2:
        palabras.append(linea.strip())
    archivo2.close()

    print(f"Alfabetos leidos ({len(alfabetos)}) posiciones: ")
    for i, a in enumerate(alfabetos, start=1):
        print(f'Posicion j={i} (simbolo #{i} desde la derecha): {a}')

    print(f"\n Palabras originales ({ len(palabras) }): ")
    print(palabras)



    resultado = radixSort(palabras, alfabetos)
    print('-----RESULTADOS---------')
    print(resultado)




main()