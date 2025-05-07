import json

def cargar_matriz_desde_json(ruta_archivo_json):
    """Convierte un archivo JSON en una matriz de adyacencia"""
    with open(ruta_archivo_json, 'r') as archivo_json:
        estructura = json.load(archivo_json)

    # Mostrar la información de la vecindad derecha
    # for i in estructura['E']:
    #     print(i)

    # Imprimir la vecindad derecha de un nodo específico (por ejemplo, 'a')
    #print("Vecindad derecha de 'a':", estructura['E'].get('a', []))

    # Imprimir la cardinalidad de la vecindad derecha de 'a'
    #print("Cardinalidad de la vecindad derecha de 'a':", len(estructura['E'].get('a', [])))

    # Convertir la estructura de JSON en una matriz de adyacencia
    cantidad_nodos = len(estructura['E'])
    matriz = [[0] * cantidad_nodos for _ in range(cantidad_nodos)]

    # Asumiendo que los nodos en el JSON son etiquetas (como 'a', 'b', etc.), los convertimos en índices numéricos
    nodos = list(estructura['E'].keys())
    nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)}

    # Construir la matriz de adyacencia
    for nodo, vecinos in estructura['E'].items():
        for vecino in vecinos:
            matriz[nodo_a_indice[nodo]][nodo_a_indice[vecino]] = 1

    return matriz

# Propiedades de la matriz

def esReflexiva(M):
    """Comprueba si la matriz es reflexiva."""
    for i in range(len(M)):
        if M[i][i] != 1:
            return False
    return True

def esSimetrica(M):
    """Comprueba si la matriz es simétrica."""
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] != M[j][i]:
                return False
    return True

def esTransitiva(M):
    """Comprueba si la matriz es transitiva."""
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 1:
                for k in range(len(M)):
                    if M[j][k] == 1 and M[i][k] == 0:
                        return False
    return True

def esAntisimetrica(M):
    """Comprueba si la matriz es antisimétrica."""
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] == 1 and M[j][i] == 1 and i != j:
                return False
    return True

def es_deOrden(M):
    """Comprueba si la matriz es de orden."""
    if esReflexiva(M) and esAntisimetrica(M) and esTransitiva(M):
        return True
    return False

def es_relDeEquivalencia(M):
    """Comprueba si la matriz es una relación de equivalencia."""
    if esReflexiva(M) and esSimetrica(M) and esTransitiva(M):
        return True
    return False


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Leer y convertir el archivo JSON en una matriz de adyacencia
    ruta_json = "01.json"
    matriz_adyacencia = cargar_matriz_desde_json(ruta_json)

    # Comprobaciones de propiedades de la matriz
    print("Es reflexiva:", esReflexiva(matriz_adyacencia))
    print("Es simétrica:", esSimetrica(matriz_adyacencia))
    print("Es transitiva:", esTransitiva(matriz_adyacencia))
    print("Es antisimétrica:", esAntisimetrica(matriz_adyacencia))
    print("Es de orden:", es_deOrden(matriz_adyacencia))
    print("Es relación de equivalencia:", es_relDeEquivalencia(matriz_adyacencia))
