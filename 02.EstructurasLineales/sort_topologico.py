import sys
from t_sort import t_sort

def ordenar_grafo(ruta):
    orden = t_sort(ruta)
    if orden is None:
        return "El grafo es cíclico"
    return orden

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python sort_topologico.py archivo_grafo")
        sys.exit(1)
    orden = ordenar_grafo(sys.argv[1])
    if isinstance(orden, str):
        print(orden)
    else:
        print(" ".join(orden))
