import json

def cargar_matriz_grafo(archivo_json):
    arch = open(archivo_json, "r")
    diccionario = json.load(arch)
    arch.close()

    lista_nodos = diccionario["P"]
    total_nodos = len(lista_nodos)
    matriz_adyacencia = []

    for i in range(total_nodos):
        fila_actual = []
        nodo_actual = lista_nodos[i]
        
        vecinos = diccionario["E"].get(nodo_actual, [])
        
        for j in range(total_nodos):
            nodo_objetivo = lista_nodos[j]
            if nodo_objetivo in vecinos:
                fila_actual.append(1)
            else:
                fila_actual.append(0)
                
        matriz_adyacencia.append(fila_actual)

    return matriz_adyacencia

def reconstruir_ruta(arreglo_padres, destino):
    ruta_final = []
    paso_actual = destino

    while paso_actual > 0:
        ruta_final.append(paso_actual)
        indice = paso_actual - 1
        paso_actual = arreglo_padres[indice]
        
    ruta_final.reverse()
    return ruta_final

def encontrar_paso(grafo_matriz, inicio, fin):
    if inicio == fin:
        print("Paso de", inicio, "a", fin, "->", [inicio])
        return [inicio]

    cantidad = len(grafo_matriz)
    pendientes = [inicio]
    
    nodos_visitados = [0] * cantidad
    nodos_padres = [0] * cantidad
    
    nodos_visitados[inicio - 1] = 1 

    while len(pendientes) != 0:
        actual = pendientes.pop(0)
        indice_actual = actual - 1

        for candidato in range(cantidad):
            hay_conexion = grafo_matriz[indice_actual][candidato]
            
            if hay_conexion == 1:
                vecino = candidato + 1
                
                if nodos_visitados[candidato] == 0:
                    nodos_visitados[candidato] = 1
                    nodos_padres[candidato] = actual
                    pendientes.append(vecino)
                    
                    if vecino == fin:
                        resultado = reconstruir_ruta(nodos_padres, fin)
                        print("Paso de", inicio, "a", fin, "->", resultado)
                        return resultado

    print("No se encontró paso de", inicio, "a", fin)
    return []

#test
grafo_1 = cargar_matriz_grafo("esDivisorDe-200.json")
encontrar_paso(grafo_1, 3, 198)
encontrar_paso(grafo_1, 6, 4)

grafo_2 = cargar_matriz_grafo("multiplos200Ref.json")
encontrar_paso(grafo_2, 7, 196)
encontrar_paso(grafo_2, 5, 5)