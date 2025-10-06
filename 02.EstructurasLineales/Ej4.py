def leerArchivo(archivo):
    palabras = []
    with open(archivo, "r") as f:
        for linea in f:
            palabra = linea.strip()
            if palabra:
                palabras.append(palabra)
    return palabras

def radixSort(palabras):
    if not palabras:
        return []
    max_len = len(max(palabras, key=len))
    # Iterar desde el último carácter al primero
    for pos in range(max_len - 1, -1, -1):
        # Crear 27 colas (a–z + vacío)
        queues = [[] for _ in range(27)]
        
        for palabra in palabras:
            if pos < len(palabra):
                # Calcular índice de la cola (a=0, b=1, ..., z=25)
                indice = ord(palabra[pos].lower()) - ord('a')
                if indice < 0 or indice > 25:  # Caracter no alfabético
                    indice = 26
            else:
                # Palabra más corta que la posición actual → cola vacío
                indice = 26
            queues[indice].append(palabra)
        
        # Reconstruir la lista concatenando las colas en orden
        palabras = []
        for cola in queues:
            while cola:
                palabras.append(cola.pop(0))
    
    return palabras

def main():
    arch="Palabras.txt"
    palabras=leerArchivo(arch)
    print("Antes de ordenar:", palabras)
    ordenadas=radixSort(palabras)
    print("Despues de ordenar:", ordenadas)

main()