import json

def cargar_csv(ruta):
  matriz = []
  archivo = open(ruta, 'r')
  for linea in archivo:
    linea = linea.strip()
    if linea != '':
      fila = []
      for num in linea.split(','):
        fila.append(int(num.strip()))
      matriz.append(fila)
  archivo.close()
  nodos = []
  for i in range(len(matriz)):
    nodos.append(str(i))
  return nodos, matriz


def cargar_json(ruta):
  archivo = open(ruta, 'r')
  datos = json.load(archivo)
  archivo.close()
  nodos = datos['P'] 
  aristas = datos['E']
  n = len(nodos)
  matriz = []
  for i in range(n):
    fila = []
    for j in range(n):
      fila.append(0)
    matriz.append(fila)
  pos = {}
  for i in range(n):
    pos[nodos[i]] = i
  for origen in aristas:
    if origen in pos:
      i = pos[origen]
      for destino in aristas[origen]:
        if destino in pos:
          j = pos[destino]
          matriz[i][j] = 1

  return nodos, matriz

def minimales(nodos, matriz):
  n = len(nodos)
  resultado = []
  for j in range(n):  # Revisar columna j
    tiene_entradas = False
    for i in range(n):
      if i != j and matriz[i][j] == 1:
        tiene_entradas = True
        break
    if not tiene_entradas:
      resultado.append(nodos[j])
  return resultado

def maximales(nodos, matriz):
  n = len(nodos)
  resultado = []
  for i in range(n):  # Revisar fila i
    tiene_salidas = False
    for j in range(n):
      if i != j and matriz[i][j] == 1:
        tiene_salidas = True
        break
    if not tiene_salidas:
      resultado.append(nodos[i])
  return resultado

def vecindad_derecha(nodo, nodos, matriz):
  n = len(nodos)
  idx = -1
  for i in range(n):
    if nodos[i] == str(nodo):
      idx = i
      break
  vecinos = []
  if idx != -1:
    for j in range(n):
      if idx != j and matriz[idx][j] == 1:
        vecinos.append(nodos[j])
  return vecinos

def vecindad_izquierda(nodo, nodos, matriz):
  n = len(nodos)
  idx = -1
  for i in range(n):
    if nodos[i] == str(nodo):
      idx = i
      break
  vecinos = []
  if idx != -1:
    for i in range(n):
      if i != idx and matriz[i][idx] == 1:
        vecinos.append(nodos[i])
  return vecinos

if __name__ == '__main__':
  nodos, matriz = cargar_json('01.json')
  print('--- EJERCICIO 1 ---')
  print('Minimales:', minimales(nodos, matriz)[:5])
  print('Maximales:', maximales(nodos, matriz)[:5])
  print("Vecindad Derecha de '1':", vecindad_derecha('1', nodos, matriz)[:5])
  print("Vecindad Izquierda de '2':", vecindad_izquierda('2', nodos, matriz)[:5])
