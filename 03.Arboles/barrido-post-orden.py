import sys

def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def postorden(a, r, i=0):
    if i >= len(a):
        return
    for k in range(1, r+1):
        postorden(a, r, r*i+k)
    print(a[i])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python barrido-post-orden.py GRADO ARCHIVO")
    postorden(leer_arbol(sys.argv[2]), int(sys.argv[1]))
