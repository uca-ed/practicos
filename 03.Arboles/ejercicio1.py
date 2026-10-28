def altura(arr, k):                           # a) altura sin recorridos
    m = len(arr) - 1                          # mayor índice ocupado
    while m >= 0 and arr[m] is None:
        m -= 1
    if m < 0:
        return -1                             # árbol vacío
    h = 0
    while m > 0:                              # subir por padres hasta la raíz
        m = (m - 1) // k
        h += 1
    return h                                  # raíz sola = altura 0
 
 
def preorden(arr, k, i=0, visitados=None):    # b) pre-orden
    if visitados is None:
        visitados = []
    if i >= len(arr) or arr[i] is None:
        return visitados
    visitados.append(arr[i])
    for j in range(1, k + 1):
        preorden(arr, k, k * i + j, visitados)
    return visitados
 
 
def postorden(arr, k, i=0, visitados=None):   # c) post-orden
    if visitados is None:
        visitados = []
    if i >= len(arr) or arr[i] is None:
        return visitados
    for j in range(1, k + 1):
        postorden(arr, k, k * i + j, visitados)
    visitados.append(arr[i])
    return visitados
 
 
def por_niveles(arr):                         # d) por niveles
    return [x for x in arr if x is not None]
 
 
def simetrico(arr, i=0, visitados=None):      # e) simétrico (solo binario)
    if visitados is None:
        visitados = []
    if i >= len(arr) or arr[i] is None:
        return visitados
    simetrico(arr, 2 * i + 1, visitados)
    visitados.append(arr[i])
    simetrico(arr, 2 * i + 2, visitados)
    return visitados
 
 
def main():
    # k = 2
    arr2 = ['A', 'B', 'C', 'D', 'E', None, 'F']
    print("k = 2:", arr2)
    print("a) altura     :", altura(arr2, 2))      # 2
    print("b) pre-orden  :", preorden(arr2, 2))    # A B D E C F
    print("c) post-orden :", postorden(arr2, 2))   # D E B F C A
    print("d) por niveles:", por_niveles(arr2))    # A B C D E F
    print("e) simétrico  :", simetrico(arr2))      # D B E A C F
 
    # k = 3
    arr3 = ['A', 'B', 'C', 'D', 'E', None, 'F', None, None, None, 'G']
    print("\nk = 3:", arr3)
    print("a) altura     :", altura(arr3, 3))      # 2
    print("b) pre-orden  :", preorden(arr3, 3))    # A B E F C D G
    print("c) post-orden :", postorden(arr3, 3))   # E F B C G D A
    print("d) por niveles:", por_niveles(arr3))    # A B C D E F G
    print("e) simétrico  : solo definido para k = 2")
 
 
main()
