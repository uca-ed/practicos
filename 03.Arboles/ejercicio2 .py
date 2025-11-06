'''
Implementacion Arboles-Ejercicio2 
Crear un árbol AVL realizando las inserciones dadas en el archivo de datos
'''

from typing import Optional, Any, Iterable, List


def nodo_nuevo(v: Any) -> dict:
    return {"v": v, "l": None, "r": None, "h": 1}  


def altura(n: Optional[dict]) -> int:
    return n["h"] if n else 0

def actualizar_altura(n: dict) -> None:
    n["h"] = 1 + max(altura(n["l"]), altura(n["r"]))

def balance(n: Optional[dict]) -> int:
    if not n:
        return 0
    return altura(n["l"]) - altura(n["r"])


def rot_der(y: dict) -> dict:
    x = y["l"]
    T2 = x["r"] if x else None
  
    x["r"] = y
    y["l"] = T2
 
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rot_izq(x: dict) -> dict:
    y = x["r"]
    T2 = y["l"] if y else None
   
    y["l"] = x
    x["r"] = T2
  
    actualizar_altura(x)
    actualizar_altura(y)
    return y

def insertar(raiz: Optional[dict], v: Any) -> dict:
 
    if raiz is None:
        return nodo_nuevo(v)
    if v < raiz["v"]:
        raiz["l"] = insertar(raiz["l"], v)
    elif v > raiz["v"]:
        raiz["r"] = insertar(raiz["r"], v)
    else:
        
        return raiz

 
    actualizar_altura(raiz)


    b = balance(raiz)

    # Izquierda-Izquierda
    if b > 1 and v < raiz["l"]["v"]:
        return rot_der(raiz)
    # Derecha-Derecha
    if b < -1 and v > raiz["r"]["v"]:
        return rot_izq(raiz)
    # Izquierda-Derecha
    if b > 1 and v > raiz["l"]["v"]:
        raiz["l"] = rot_izq(raiz["l"])
        return rot_der(raiz)
    # Derecha-Izquierda
    if b < -1 and v < raiz["r"]["v"]:
        raiz["r"] = rot_der(raiz["r"])
        return rot_izq(raiz)

    return raiz

def insertar_varios(raiz: Optional[dict], datos: Iterable[Any]) -> Optional[dict]:
    for x in datos:
        raiz = insertar(raiz, x)
    return raiz


def inorder(n: Optional[dict], out: List[Any]) -> None:
    if not n: return
    inorder(n["l"], out)
    out.append(n["v"])
    inorder(n["r"], out)

def preorden(n: Optional[dict], out: List[Any]) -> None:
    if not n: return
    out.append(n["v"])
    preorden(n["l"], out)
    preorden(n["r"], out)


def cargar_txt(ruta: str) -> list:

    vals = []
    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:  
                continue
            try:
                vals.append(int(s))
            except ValueError:
                vals.append(s)
    return vals

def cargar_csv(ruta: str, columna: str = "valor", sep: str = ",") -> list:
    import csv
    vals = []
    with open(ruta, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter=sep)
        for row in r:
            s = row[columna]
            try:
                vals.append(int(s))
            except ValueError:
                vals.append(s)
    return vals


if __name__ == "__main__":
    raiz = None
 
    datos = [30, 10, 50, 5, 20, 40, 60, 35, 45]
    raiz = insertar_varios(raiz, datos)

    io, po = [], []
    inorder(raiz, io)
    preorden(raiz, po)
    print("In-orden (ordenado):", io)
    print("Pre-orden (estructura):", po)
    print("Altura:", altura(raiz))

    # Con archivo
    vals = cargar_txt("inserciones.txt")
    raiz = insertar_varios(None, vals) 

    io2, po2 = [], []
    inorder(raiz, io2)
    preorden(raiz, po2)
    print("\nDesde archivo txt")
    print("In-orden (ordenado):", io2)
    print("Pre-orden (estructura):", po2)
    print("Altura:", altura(raiz))

