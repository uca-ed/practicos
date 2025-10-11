""""
4. Implementar Radix Sort y ordenar las palabras de los archivos indicados.  
"""

from queue import Queue

def cargar_cola_desde_archivo(nombre_archivo):
    cola = Queue()
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read().strip()
        palabras = contenido.split(",")
        for palabra in palabras:
            cola.put(palabra)
    return cola

def imprimir_cola(cola):
    elementos = list(cola.queue)
    for elem in elementos:
        print(elem)

def radix_sort(cola):
    if cola.empty():
        return

    max_len = max(len(palabra) for palabra in list(cola.queue))
    for pos in range(max_len - 1, -1, -1):
        aux = [Queue() for _ in range(26)]

        while not cola.empty():
            palabra = cola.get()
            char = palabra[pos] if pos < len(palabra) else ' '
            index = ord(char.lower()) - ord('a') if char.isalpha() else 25
            aux[index].put(palabra)

        for aux in aux:
            while not aux.empty():
                cola.put(aux.get())

if __name__ == "__main__":

    mi_cola = cargar_cola_desde_archivo("ejemplo4.txt")
    print("Elementos de la cola:")
    imprimir_cola(mi_cola)
    
    radix_sort(mi_cola)
    print("\nElementos de la cola ordenados:")
    imprimir_cola(mi_cola)
