
from collections import deque

def radix_sort_con_colas(palabras):
    # paso a minusculas primero y saco los espacios si es q el usuario puso
    palabras = [p.strip().lower() for p in palabras]
    if not palabras:
        return []

    max_len = max(len(p) for p in palabras)

    # Pasadas de derecha a izquierda
    for pos in range(max_len - 1, -1, -1):
        # creo 27 colas ya q el abecedario tiene 26 letras + 1 para vacio
        cola = [deque() for _ in range(27)]

        # Encolar cada palabra en la cola correspondiente
        for palabra in palabras:
            if pos < len(palabra):
                index = ord(palabra[pos]) - ord('a') + 1  # "a"->1 ... "z"->26
            else:
                index = 0  # vacío (menor que 'a')
            cola[index].append(palabra)

        # Reconstruir en orden
        nuevas = []
        for q in cola:
            while q:
                nuevas.append(q.popleft())
        palabras = nuevas
    return palabras


def main():
    # Leo el archivo csv
    with open("ejercicio4.txt", "r", encoding="utf-8") as f:
        linea = f.read().strip()

    # pone en la lista las palabras sacando los espacios y separa por comas
    palabras = [p.strip() for p in linea.split(",") if p.strip()]

    ordenadas = radix_sort_con_colas(palabras)

    print("Entrada:", palabras)
    print("Salida ordenada:", ordenadas)

if __name__ == "__main__":
    main()
