def leer_grafo(archivo):
    g = {}
    grado = {}
    with open(archivo) as f:
        for linea in f:
            a, b = linea.strip().split()
            g.setdefault(a, []).append(b)
            grado[b] = grado.get(b, 0) + 1
            grado.setdefault(a, 0)
    return g, grado
#Con leer grafo uso el diccionario g para poner las conexiones de los nodos
# En el diccionario grado pongo el grado de cada nodo
def t_sort(g, grado):
    cola = [n for n in grado if grado[n] == 0]
    orden = []
    while cola:
        n = cola.pop()
        orden.append(n)
        for v in g.get(n, []):
            grado[v] -= 1
            if grado[v] == 0:
                cola.append(v)
    if len(orden) != len(grado):
        print("Cíclico")
    else:
        print("Orden:", " → ".join(orden))
#aplico t-sort para mostrar el orden topologico del grafo que paso por grafoEj5.txt
#en el caso de que el grafo no sea aciclico, printea la palabra ciclico

def main():
    g, grado = leer_grafo("grafoEj5.txt")
    t_sort(g, grado)
    
main()