#Ejercicio 5: Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. De no ser posible calcularlo, indicar que la estructura es cíclica.

def leer_grafo_desde_archivo(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or ':' not in linea:
                continue
            nodo, vecinos_str = linea.split(':', 1)
            vecinos = vecinos_str.strip().split() if vecinos_str.strip() else []
            grafo[nodo.strip()] = vecinos
    return grafo

def t_sort(grafo):
    grado_entrada = {nodo: 0 for nodo in grafo}
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if vecino not in grado_entrada:
                grado_entrada[vecino] = 0
            grado_entrada[vecino] += 1

    cola = [nodo for nodo in grado_entrada if grado_entrada[nodo] == 0]
    orden = []

    while cola:
        nodo = cola.pop(0)
        orden.append(nodo)
        for vecino in grafo.get(nodo, []):
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)

    if len(orden) != len(grado_entrada):
        print("La estructura es cíclica.")
        return None
    return orden

def main():
    nombre_archivo = 'grafo.txt'
    grafo = leer_grafo_desde_archivo(nombre_archivo)
    resultado = t_sort(grafo)
    if resultado:
        print("Orden topológico:", resultado)

if __name__ == "__main__":
    main()
