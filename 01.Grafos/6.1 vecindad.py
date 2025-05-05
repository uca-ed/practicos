#----------------Vecindad Izquierda
def vecindadIzquierda (E,grafo):
    rta = grafo.get(E[0])   
    print("La vecindad izquierda es", rta)
    return rta

#----------------Vecindad Izquierda
def vecindadDerecha (E,grafo):
    lista = []
    for key in (grafo.keys()):
        for value in grafo.get(key):
            if (value == E[1]):
                lista.append(key)
    print("La vecindad derecha es", lista)
    return lista


grafo = {
    'A':['E','I'],
    'E':['I','A'],
    'I':['O'],
    'O':['A']
    }

print(grafo)
vecindadIzquierda (('A','E'),grafo)
vecindadDerecha(('A','E'),grafo)