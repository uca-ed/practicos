import argparse

def generar_arbol_por_niveles(r: int, h: int):
    """
    Genera e imprime un árbol lleno de grado r (par) y altura h, representado como un arreglo, según la teórica vista en clase
  
    """
    if r % 2 != 0:
        raise ValueError("El grado 'r' debe ser un número par.")
    if h < 1:
        raise ValueError("La altura 'h' debe ser al menos 1.")

    nodos_en_ultimo_nivel = r ** (h - 1)
    rango_total = 10 * nodos_en_ultimo_nivel # los separo multiplicando por 10 para tener espacio y que no se solapen números
    
    for nivel in range(h):
        nodos_en_nivel = r ** nivel
        
        # Tamaño del bloque asignado a cada nodo en el nivel actual
        tamano_bloque = rango_total // nodos_en_nivel
        
        #elementos_nivel = []
        for i in range(nodos_en_nivel):
            # El valor del nodo es el punto medio del bloque i
            valor_nodo = i * tamano_bloque + tamano_bloque // 2
            print(f"{valor_nodo}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int, help="Grado del árbol")
    parser.add_argument("h", type=int, help="Altura del árbol")
    args = parser.parse_args()

    generar_arbol_por_niveles(r=args.r, h=args.h)
