import json

def cargar_grafo(ruta_json):
  archivo = open(ruta_json, 'r')
  datos = json.load(archivo)
  archivo.close()

  nodos = datos['P']
  aristas = datos['E']
  n = len(nodos)

  matriz = []
  for i in range(n):
    matriz.append([0] * n)

  pos = {}
  for i in range(n):
    pos[nodos[i]] = i

  for u in aristas:
    if u in pos:
      for v in aristas[u]:
        if v in pos:
          matriz[pos[u]][pos[v]] = 1

  return nodos, matriz


def es_reflexiva(matriz):
  n = len(matriz)
  for i in range(n):
    if matriz[i][i] != 1:
      return False
  return True


def es_simetrica(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(n):
      if matriz[i][j] == 1 and matriz[j][i] != 1:
        return False
  return True


def es_antisimetrica(matriz):
  n = len(matriz)
  for i in range(n):
    for j in range(n):
      if i != j and matriz[i][j] == 1 and matriz[j][i] == 1:
        return False
  return True


def es_transitiva(matriz):
  n = len(matriz)
  for i in range(n):
    for k in range(n):
      if matriz[i][k] == 1:
        for j in range(n):
          if matriz[k][j] == 1 and matriz[i][j] != 1:
            return False
  return True


def clasificar_grafo(ruta_json):
  nodos, matriz = cargar_grafo(ruta_json)

  refl = es_reflexiva(matriz)
  sim = es_simetrica(matriz)
  anti = es_antisimetrica(matriz)
  trans = es_transitiva(matriz)

  print(f'=== Análisis de: {ruta_json} ===')
  print(f'Reflexiva:     {refl}')
  print(f'Simétrica:     {sim}')
  print(f'Antisimétrica: {anti}')
  print(f'Transitiva:    {trans}')

  if refl and anti and trans:
    print('-> Es una RELACIÓN DE ORDEN (Orden Parcial)')
  elif refl and sim and trans:
    print('-> Es una RELACIÓN DE EQUIVALENCIA')
  else:
    print('-> No es ni de Orden ni de Equivalencia')
  print()


if __name__ == '__main__':
  clasificar_grafo('01.json')
