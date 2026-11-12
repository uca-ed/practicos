import sys

def leer_arbol(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def por_niveles(a):
    # El archivo generado ya esta almacenado por niveles.
    for valor in a:
        print(valor)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python barrido-por-niveles.py GRADO ARCHIVO")
    int(sys.argv[1])  # conserva la interfaz del script de pruebas
    por_niveles(leer_arbol(sys.argv[2]))
