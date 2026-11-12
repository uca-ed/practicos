import sys

def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def simetrico(a, i=0):
    if i >= len(a):
        return
    simetrico(a, 2*i+1)
    print(a[i])
    simetrico(a, 2*i+2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python barrido-simetrico.py ARCHIVO")
    simetrico(leer_arbol(sys.argv[1]))
