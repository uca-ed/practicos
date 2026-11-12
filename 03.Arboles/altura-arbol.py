import sys

def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

# Para un arbol r-ario lleno, n = 1 + r + ... + r**(h-1).
def altura(n, r):
    if r < 2:
        raise ValueError("El grado debe ser al menos 2")
    if n == 0:
        return 0
    cantidad = 0
    nivel = 0
    while cantidad < n:
        cantidad += r ** nivel
        nivel += 1
    if cantidad != n:
        raise ValueError("El arreglo no representa un arbol r-ario lleno")
    return nivel

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python altura-arbol.py GRADO ARCHIVO")
    print(altura(len(leer_arbol(sys.argv[2])), int(sys.argv[1])))
