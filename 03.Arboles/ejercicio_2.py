with open("datos.txt", "w") as f:
    f.write("\n".join(["30", "20", "40", "10", "25", "35", "50"]))

def altura(nodo):
    return nodo["altura"] if nodo else 0

def balance(nodo):
    if not nodo:
        return 0
    return altura(nodo["izq"]) - altura(nodo["der"])

# Rotación derecha
def rotar_derecha(y):
    x = y["izq"]
    T2 = x["der"]
    x["der"] = y
    y["izq"] = T2
    y["altura"] = 1 + max(altura(y["izq"]), altura(y["der"]))
    x["altura"] = 1 + max(altura(x["izq"]), altura(x["der"]))
    return x

# Rotación izquierda
def rotar_izquierda(x):
    y = x["der"]
    T2 = y["izq"]
    y["izq"] = x
    x["der"] = T2
    x["altura"] = 1 + max(altura(x["izq"]), altura(x["der"]))
    y["altura"] = 1 + max(altura(y["izq"]), altura(y["der"]))
    return y

# AVL
def insertar(nodo, valor):
    if not nodo:
        return {"valor": valor, "izq": None, "der": None, "altura": 1}

    if valor < nodo["valor"]:
        nodo["izq"] = insertar(nodo["izq"], valor)
    else:
        nodo["der"] = insertar(nodo["der"], valor)

    nodo["altura"] = 1 + max(altura(nodo["izq"]), altura(nodo["der"]))
    b = balance(nodo)


    if b > 1 and valor < nodo["izq"]["valor"]:
        return rotar_derecha(nodo)
    if b < -1 and valor > nodo["der"]["valor"]:
        return rotar_izquierda(nodo)
    if b > 1 and valor > nodo["izq"]["valor"]:
        nodo["izq"] = rotar_izquierda(nodo["izq"])
        return rotar_derecha(nodo)
    if b < -1 and valor < nodo["der"]["valor"]:
        nodo["der"] = rotar_derecha(nodo["der"])
        return rotar_izquierda(nodo)

    return nodo

# Recorrido orden
def orden(nodo):
    if nodo:
        orden(nodo["izq"])
        print(nodo["valor"], end=" ")
        orden(nodo["der"])

raiz = None
with open("datos.txt", "r") as f:
    for linea in f:
        num = int(linea.strip())
        raiz = insertar(raiz, num)

print("Recorrido del árbol AVL:")
orden(raiz)