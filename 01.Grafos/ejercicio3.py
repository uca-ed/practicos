import json

def cargar_grafo_lista(ruta_json):
  archivo = open(ruta_json, 'r')
  datos = json.load(archivo)
  archivo.close()
  return datos.get('E', {})

def obtener_paso(aristas, inicio, fin):
  inicio = str(inicio)
  fin = str(fin)

  if inicio == fin:
    return [inicio]

  cola = [[inicio]]
  visitados = set([inicio])

  while len(cola) > 0:
    camino = cola.pop(0)
    nodo_actual = camino[-1]

    vecinos = aristas.get(nodo_actual, [])
    for vecino in vecinos:
      if vecino == fin:
        return camino + [vecino]

      if vecino not in visitados:
        visitados.add(vecino)
        nuevo_camino = list(camino)
        nuevo_camino.append(vecino)
        cola.append(nuevo_camino)

  return None 

if __name__ == '__main__':
  grafo_aristas = cargar_grafo_lista('esDivisorDe-200.json')

  origen = '2'
  destino = '200'

  paso = obtener_paso(grafo_aristas, origen, destino)

  print('--- EJERCICIO 3 ---')
  if paso:
    print(f'Paso de {origen} a {destino}:', ' -> '.join(paso))
  else:
    print(f'No existe paso de {origen} a {destino}')
