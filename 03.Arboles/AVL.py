import sys
class NodoAVL:
  def __init__(self, clave):
    self.clave = clave
    self.izq = None
    self.der = None
    self.altura = 1


def obtener_altura(nodo):
  return nodo.altura if nodo else 0

def actualizar_altura(nodo):
  nodo.altura = 1 + max(obtener_altura(nodo.izq), obtener_altura(nodo.der))

def obtener_balance(nodo):
  if not nodo:
    return 0
  return obtener_altura(nodo.izq) - obtener_altura(nodo.der)

def rotacion_derecha(y):
  x = y.izq
  t2 = x.der
  x.der = y
  y.izq = t2
  actualizar_altura(y)
  actualizar_altura(x)
  return x

def rotacion_izquierda(x):
  y = x.der
  t2 = y.izq
  y.izq = x
  x.der = t2
  actualizar_altura(x)
  actualizar_altura(y)
  return y

def balancear_nodo(nodo, clave):
  balance = obtener_balance(nodo)
  if balance > 1 and clave < nodo.izq.clave:
    return rotacion_derecha(nodo)
  if balance < -1 and clave > nodo.der.clave:
    return rotacion_izquierda(nodo)
  if balance > 1 and clave > nodo.izq.clave:
    nodo.izq = rotacion_izquierda(nodo.izq)
    return rotacion_derecha(nodo)
  if balance < -1 and clave < nodo.der.clave:
    nodo.der = rotacion_derecha(nodo.der)
    return rotacion_izquierda(nodo)
  return nodo

def insertar_iterativo(raiz, clave):
  if raiz is None:
    return NodoAVL(clave)
  pila_ancestros = []
  actual = raiz
  while actual is not None:
    if clave == actual.clave:
      return raiz  
    pila_ancestros.append(actual)
    if clave < actual.clave:
      if actual.izq is None:
        actual.izq = NodoAVL(clave)
        break
      actual = actual.izq
    else:
      if actual.der is None:
        actual.der = NodoAVL(clave)
        break
      actual = actual.der
  nueva_subraiz = None
  while len(pila_ancestros) > 0:
    nodo_actual = pila_ancestros.pop()
    actualizar_altura(nodo_actual)
    if nueva_subraiz is not None:
      if nodo_actual.izq and nodo_actual.izq.clave == clave_afectada:
        nodo_actual.izq = nueva_subraiz
      elif nodo_actual.der and nodo_actual.der.clave == clave_afectada:
        nodo_actual.der = nueva_subraiz
      actualizar_altura(nodo_actual)
      nueva_subraiz = None
    balance = obtener_balance(nodo_actual)
    if balance > 1 or balance < -1:
      clave_afectada = nodo_actual.clave
      nueva_subraiz = balancear_nodo(nodo_actual, clave)
      if len(pila_ancestros) == 0:
        raiz = nueva_subraiz
        break
  return raiz

def imprimir_por_niveles(raiz):
  if not raiz:
    print("Árbol vacío")
    return

  cola = [(raiz, 0)]
  nivel_actual = -1

  while len(cola) > 0:
    nodo, nivel = cola.pop(0)

    if nivel != nivel_actual:
      nivel_actual = nivel
      print(f"\n[Nivel {nivel}]:", end=" ")

    hijo_i = f"I:{nodo.izq.clave}" if nodo.izq else "I:-"
    hijo_d = f"D:{nodo.der.clave}" if nodo.der else "D:-"
    print(f"({nodo.clave} | h={nodo.altura} | {hijo_i},{hijo_d})", end="  ")

    if nodo.izq:
      cola.append((nodo.izq, nivel + 1))
    if nodo.der:
      cola.append((nodo.der, nivel + 1))
  print("\n")


import os

if __name__ == "__main__":
  # Obtiene el directorio exacto donde reside este script avl.py
  dir_script = os.path.dirname(os.path.abspath(__file__))

  # Si pasaste un archivo por argumento usa ese; si no, busca datos_avl.txt en la misma carpeta del script
  if len(sys.argv) > 1:
    ruta_archivo = sys.argv[1]
  else:
    ruta_archivo = os.path.join(dir_script, "datos_avl.txt")

  raiz = None
  print(f"Leyendo '{ruta_archivo}' de forma iterativa...\n")
  try:
    with open(ruta_archivo, "r") as archivo:
      for linea in archivo:
        linea = linea.strip()
        if linea and not linea.startswith("#"):
          valor = int(linea)
          print(f"Insertando: {valor}")
          raiz = insertar_iterativo(raiz, valor)

    print("\n=== ÁRBOL AVL FINAL (RECORRIDO POR NIVELES) ===")
    imprimir_por_niveles(raiz)

  except FileNotFoundError:
    print(f"[ERROR] No se encontró '{ruta_archivo}'.")