#sorting_topologico.py

def counting_sort_estable(lista_palabras, pos):
    salida = [None] * len(lista_palabras)
    conteo = [0] * 256  
    
    for palabra in lista_palabras:
        char_val = ord(palabra[pos]) if pos < len(palabra) else 32
        conteo[char_val] += 1
        
    for i in range(1, 256):
        conteo[i] += conteo[i - 1]
        
    for palabra in reversed(lista_palabras):
        char_val = ord(palabra[pos]) if pos < len(palabra) else 32
        conteo[char_val] -= 1
        salida[conteo[char_val]] = palabra
        
    return salida

def radix_sort_palabras(lista_palabras):
    if not lista_palabras: return lista_palabras
    L = max(len(palabra) for palabra in lista_palabras)
    
    for pos in range(L - 1, -1, -1):
        lista_palabras = counting_sort_estable(lista_palabras, pos)
    return lista_palabras


def calcular_t_sort(nodos, adyacencia):
    in_degree = {str(n): 0 for n in nodos}
    
    for u in adyacencia:
        for v in adyacencia[u]:
            v_str = str(v)
            if v_str in in_degree:
                in_degree[v_str] += 1
                
    cola = [n for n in in_degree if in_degree[n] == 0]
    resultado = []
    
    while cola:
        u = cola.pop(0)
        resultado.append(u)
        
        if u in adyacencia:
            for vecino in adyacencia[u]:
                v_str = str(vecino)
                if v_str in in_degree:
                    in_degree[v_str] -= 1
                    if in_degree[v_str] == 0:
                        cola.append(v_str)
                        
    if len(resultado) < len(nodos):
        return "Error: La estructura es cíclica (no se puede calcular T-Sort)"
    return resultado