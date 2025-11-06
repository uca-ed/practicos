#Para cada nodo,la diferencia de alturas entre su subárbol izquierdo y derecho es como máximo 1.

def crear_nodo(valor):
    return {"valor": valor, 
            "izq": None, 
            "der": None, 
            "altura": 1}


def obtener_altura(nodo):
    res = 0 
    if nodo:
        res = nodo["altura"]
    return res #si no hay subarbol devuelve 0


def obtener_balance(nodo):
    if not nodo:
        return 0
    return obtener_altura(nodo["izq"]) - obtener_altura(nodo["der"]) # Si no da 0 o 1, está desequilibrado


def rotar_derecha(z):
    y = z["izq"]

    z["izq"] = y["der"]
    y["der"] = z

    z["altura"] = 1 + max(obtener_altura(z["izq"]), obtener_altura(z["der"]))
    y["altura"] = 1 + max(obtener_altura(y["izq"]), obtener_altura(y["der"]))

    return y


def rotar_izquierda(z):
    y = z["der"]

    z["der"] = y["izq"]
    y["izq"] = z

    z["altura"] = 1 + max(obtener_altura(z["izq"]), obtener_altura(z["der"]))
    y["altura"] = 1 + max(obtener_altura(y["izq"]), obtener_altura(y["der"]))

    return y


def insertar(raiz, valor):

    if not raiz:
        return crear_nodo(valor)
    elif valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    else:
        raiz["der"] = insertar(raiz["der"], valor)


    raiz["altura"] = 1 + max(obtener_altura(raiz["izq"]), obtener_altura(raiz["der"]))


    balance = obtener_balance(raiz)
  
    if balance > 1 and valor < raiz["izq"]["valor"]: # Izquierda-Izquierda
        return rotar_derecha(raiz)
    
    
    if balance < -1 and valor > raiz["der"]["valor"]: # Derecha-Derecha
        return rotar_izquierda(raiz)
    
    
    if balance > 1 and valor > raiz["izq"]["valor"]: # Izquierda-Derecha
        raiz["izq"] = rotar_izquierda(raiz["izq"])
        return rotar_derecha(raiz)
    
    
    if balance < -1 and valor < raiz["der"]["valor"]: # Derecha-Izquierda
        raiz["der"] = rotar_derecha(raiz["der"])
        return rotar_izquierda(raiz)

    return raiz


def preorden(nodo):
    if not nodo:
        return []
    return [nodo["valor"]] + preorden(nodo["izq"]) + preorden(nodo["der"])


def ejecutar(nombre, datos):

    raiz = None

    for valor in datos:
        raiz = insertar(raiz, valor)

    print(f"Recorrido Pre-Orden {nombre}: {preorden(raiz)}")


def main():
    arbol1 = [2, [10, 5, 20, 3, 7, 15, 25]]
    arbol2 = [3, ['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    arbol3 = [4, [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    arbol4 = [2, [10, 5, 20, 3, 7, 15]]

    ejecutar("Arbol 1", arbol1[1])
    ejecutar("Arbol 2", arbol2[1])
    ejecutar("Arbol 3", arbol3[1])
    ejecutar("Arbol 4", arbol4[1])

main()
