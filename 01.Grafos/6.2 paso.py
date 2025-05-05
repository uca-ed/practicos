#----------------Paso
def miPaso (nodoPartir, nodoLlegar, grafo):
    vecinos = grafo.get(nodoPartir)
    lista=[nodoPartir]
    for valor in vecinos:
        if (valor==nodoLlegar):
            return [nodoPartir,nodoLlegar]
        else:
            while (valor!=nodoLlegar):
                lista=[nodoPartir]
                lista.append(valor)
                vecinos = grafo.get(valor)
                for valor in vecinos:
                    lista.append(valor)
                    if (valor==nodoLlegar):
                        return lista

grafo = {
    'A':['E','I'],
    'E':['I','A'],
    'I':['O'],
    'O':['A']
    }

print(grafo)
x=miPaso('A','O',grafo)
print(x)
x=miPaso('A','I',grafo)
print(x)