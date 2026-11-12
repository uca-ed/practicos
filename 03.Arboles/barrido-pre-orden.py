import sys

def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def preorden(a, r, i=0):
    if i >= len(a):
        return
    print(a[i])
    for k in range(1, r+1):
        preorden(a, r, r*i+k)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python barrido-pre-orden.py GRADO ARCHIVO")
    preorden(leer_arbol(sys.argv[2]), int(sys.argv[1]))
