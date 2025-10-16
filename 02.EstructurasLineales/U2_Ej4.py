def radix_sort(data):
    pilas_aux = [[] for _ in range(10)]
    for item in data:
        indice = item[1]
        pilas_aux[indice].append(item)
    data = [elemento for pila in pilas_aux for elemento in pila]
    #primero ordenamos lo menos significativo(la posicion 1 que serian los numeros)
    #usamos pilas para ir separando y luego agregar segun los numeros ordenados
    
    pilas_aux = [[] for _ in range(26)]
    for item in data:
        indice = ord(item[0]) - ord('a')
        pilas_aux[indice].append(item)
    data = [elemento for pila in pilas_aux for elemento in pila]
    #despues ordenamos por lo mas significativo (la posicion 0 que serian las letras) y nos deberia entregar todo el diccionario ordenado

    return data

def main():
    diccionario = [ ['a', 3], ['c', 1], ['b', 7], ['d', 2], ['a', 5], ['c', 4], ['b', 6], ['d', 9], ['a', 8], ['b', 0] ]
    #no hbaia archivos para leer asi que defini un diccionario propio para poder aplicar radix sort
    print("Original:")
    for x in diccionario:
        print(x)

    ordenado = radix_sort(diccionario)

    print("\nOrdenado por letra y número:")
    for x in ordenado:
        print(x)

main()
