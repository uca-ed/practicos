#Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. 
#De no ser posible calcularlo, indicar que la estructura es cíclica.
#La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser la secuencia generada por t-sort.
#El 7 es practicamente lo mismo que este asi que supongo que para ambos aplicaria este algoritmo 

def calcular_tsort(grafo,nodos,entrada):
    tsort=[]
    cola=[nodo for nodo in nodos if entrada[nodo]==0]
    while cola:
        nodo=cola.pop(0)
        tsort.append(nodo)
        for vecino in grafo.get(nodo,[]):
            entrada[vecino]-=1
            if entrada[vecino]==0:
                cola.append(vecino)
    if len(tsort)!=len(nodos):
        return "El grafo es cíclico"
    res="Secuencia: " + " -> ".join(tsort)
    return res

def main():
    grafo={}
    entrada={}
    nodos=set()
    with open(r"C:\Users\danie\OneDrive\Documentos\estructura de datos\practica2\ej5.txt") as f:
        for linea in f:
                linea=linea.strip()
                if not linea:
                    continue
                origen, destino=[x.strip() for x in linea.split(",")]
                nodos.add(origen)
                nodos.add(destino)
                if origen not in grafo:
                    grafo[origen]=[]
                if origen not in entrada:
                    entrada[origen]=0
                if destino not in entrada:
                    entrada[destino]=0
                grafo[origen].append(destino)
                entrada[destino]+=1
    print(calcular_tsort(grafo,nodos,entrada))

main()