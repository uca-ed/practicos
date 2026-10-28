import sys
from collections import deque
 

alfabetos = [
    ('O', 'E', 'B', 'C'),   # posicion más significativa
    (1, 2),                  
    (1, 2, 3, 4),             # posicion 2, menos significativa
]
 
 
def armar_indices(alfabetos):
    indices = []
    for alfabeto in alfabetos:
        tabla = {}
        i = 0
        for simbolo in alfabeto:
            tabla[simbolo] = i
            i = i + 1
        indices.append(tabla)
    return indices
 
 
def radix_sort(palabras, alfabetos):
    indices = armar_indices(alfabetos)
    p = len(alfabetos)
 
    Q = deque(palabras) #crea la cola con las palabras NO ordenadas
    for pos in range(p - 1, -1, -1): #lo recorro al revés
        r = len(alfabetos[pos])  # tamano del alfabeto de esta posicion

        Qaux = []
        for i in range(r):
            Qaux.append(deque())
 
        while Q:
            palabra = Q.popleft() #es igual que un dequeue
            simbolo = palabra[pos]
            d = indices[pos][simbolo]
            Qaux[d].append(palabra)

        for cola in Qaux:
            for elemento in cola:
                Q.append(elemento)
 
    return list(Q)
 
 
def convertir_campo(campo, alfabeto):
    campo = campo.strip()
    if isinstance(alfabeto[0], int):
        return int(campo)
    return campo
 
 
def cargar_archivo(nombre, alfabetos):
    palabras = []
    try:
        with open(nombre, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
 
                campos = linea.split(",")
                palabra = []
                for pos in range(len(alfabetos)):
                    valor = convertir_campo(campos[pos], alfabetos[pos])
                    palabra.append(valor)
                palabras.append(tuple(palabra))
    except OSError:
        print(f"No se pudo abrir '{nombre}'", file=sys.stderr)
 
    return palabras
 
 
def main():
    if len(sys.argv) < 2:
        print(f"Uso: python3 {sys.argv[0]} archivo.txt", file=sys.stderr)
        sys.exit(1)
 
    palabras = cargar_archivo(sys.argv[1], alfabetos)
 
    if not palabras:
        print("No se cargaron palabras.")
        return
 
    ordenadas = radix_sort(palabras, alfabetos)
 
    print("Palabras ordenadas:")
    for palabra in ordenadas:
        print(palabra)
 
 
if __name__ == "__main__":
    main()