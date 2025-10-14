def topological_sort(grafo):
    visitado = {}
    orden = []
    
    def dfs(nodo):
        if visitado.get(nodo) == 1: 
            return False
        if visitado.get(nodo) == 2: 
            return True
            
        visitado[nodo] = 1  
        for vecino in grafo.get(nodo, []):
            if not dfs(vecino):
                return False
                
        visitado[nodo] = 2  
        orden.append(nodo)
        return True
    
    
    for nodo in grafo:
        if nodo not in visitado:
            if not dfs(nodo):
                return None  
                
    orden.reverse()
    return orden

# Ejemplo de uso:
if __name__ == "__main__":
    grafo_ejemplo = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    
    resultado = topological_sort(grafo_ejemplo)
    
    if resultado is None:
        print("El grafo tiene ciclos")
    else:
        print("Orden topológico:", resultado)
    