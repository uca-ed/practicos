grafo1 = [
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,1]
]

grafo2 = [
    [0,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0]
]

grafo3 = [
    [0,0,0,0,0,1],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [1,0,0,0,0,0]
]

grafo4 = [
    [0,0,1,0,0,1],
    [1,1,1,0,0,0],
    [0,1,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [1,0,0,0,0,0]
]

def minimales(mat):
  n = len(mat)
  minimos = []
  
  for j in range(n):
    es_minimal = True
    
    for i in range(n):
      if i!=j and mat[i][j]==1:
        es_minimal = False
        break

    if es_minimal:
        minimos.append(j)

  return minimos

def maximal(mat):
  n = len(mat)
  max = []
  
  for j in range(n):
    es_maximal = True

    for i in range(n):
        if i!=j and mat[j][i]==1:
            es_maximal = False
            break

    if es_maximal:
        max.append(j)

  return max

def vencidad_derecha(mat, x):
    n = len(mat)
    vd = []
    
    for i im range(n):
        if(mat[x][i] == 1)
            vd.add(i);

    return vd;

        

print("Minimales G1:", minimales(grafo1))
print("Minimales G2:", minimales(grafo2))
print("Minimales G3:", minimales(grafo3))
print("Minimales G4:", minimales(grafo4))
print("Maximales G1:", maximal(grafo1))
print("Maximales G2:", maximal(grafo2))
print("Maximales G3:", maximal(grafo3))
print("Maximales G4:", maximal(grafo4))
print("Vecindad derecha de 0 en G4:", vecindad_derecha(grafo4, 0))
