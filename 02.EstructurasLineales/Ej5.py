def sort_topologico(grafo):
    listado_grados=[]
    grados_entrada=0
    lista_nodos_letra=[]
    t_sort=[]
    for i in range(len(grafo)):
        lista_nodos_letra.append(chr(ord('a')+i))
    while grafo:
        for i in range(len(grafo)):
            grados_entrada=0
            for j in range(len(grafo)):
                grados_entrada+=grafo[j][i]
            listado_grados.append(grados_entrada)
        menor=min(listado_grados)
        if menor!=0:
            print('el grafo tiene ciclo, no se puede calcular el sort topologico')
            return
        nodo=listado_grados.index(menor)
        grafo.pop(nodo)
        t_sort.append(lista_nodos_letra.pop(nodo))
        for lista in grafo:
            lista.pop(nodo)
        listado_grados=[]
    print('el orden topologico del grafo es: ',t_sort)
def main():
    grafo = []
    with open('grafo.txt', 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea == '':
                continue
            fila = [int(x) for x in linea.split(',')]
            grafo.append(fila)

    sort_topologico(grafo)
main()
#lo que hace el codigo es que suma cada columna de la matriz para ver los grados de entrada de cada nodo, el que tenga grado de entrada cero
#es el minimal por lo que se elimina tanto la columna como la fila del nodo.
#al mismo tiempo se lleva una lista auxiliar que nombra a cada uno de los nodos con una letra, cuando se elimina (por indice) el nodo de la matriz,
#tambien se elimina el mismo indice de la lista de letras, y se guarda esa letra en la lista de t_sort.
#esto se hace porque a medida que voy eliminando de la matriz, las filas(nodos) se van moviendo de lugar y pierdo su posicion original, pero al tener
#la lista de letras que se va moviendo de la misma forma que la matriz puedo conservar lo que seria su posicion original que la representa la letra
#que se le coloco al principio.