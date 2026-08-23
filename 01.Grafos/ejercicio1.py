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

print("Minimales G1:", minimales(grafo1))
print("Minimales G2:", minimales(grafo2))
print("Minimales G3:", minimales(grafo3))
print("Minimales G4:", minimales(grafo4))

