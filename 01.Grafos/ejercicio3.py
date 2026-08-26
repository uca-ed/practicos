import json

def cargar_estructura(nombre_arch):
    archivo = open(nombre_arch, "r")
    estructura=json.load(archivo)
    archivo.close()
    return estructura

def agregar_vecindad_drch(nodo, arcos, fin):
    vecinos = arcos.get(nodo, [])
    if fin in vecinos:
        return None, True
    else:
        pares_nodos=[]
        for item in vecinos:
            pares_nodos.append((item, nodo))
        return pares_nodos, False

def obtenerRecorrido(abrir, cerrar, inicio):
    pasos=[cerrar[0][0], cerrar[0][1]]
    referencia=cerrar[0][1]
    while referencia != inicio:
        for pares in abrir:
            if pares[1]==referencia:
                pasos.append(pares[1])
                referencia=pares[0]
    pasos.append(inicio)
    pasos.reverse()
    return pasos


def algoritmo_paso(inicio, fin, estructura):
    bandera=0
    nodos=estructura["P"]
    arcos=estructura["E"]
    abrir = [(inicio, None)]
    cerrar = []
    while(bandera==0):
        index=(len(abrir)-1)
        nodo=abrir[index][0]
        nuevos_vecinos=agregar_vecindad_drch(nodo, arcos, fin)
        abrir.pop(index)
        if nuevos_vecinos[1]:
            cerrar.append((fin,nodo))
            bandera=1
        else:
            abrir.extend(nuevos_vecinos[0])
        
    pasos=obtenerRecorrido(abrir, cerrar, inicio)
    return pasos

def main():
    estructura= cargar_estructura("esDivisorDe-200")
    pasos=algoritmo_paso("12","8",estructura)
    print(pasos)

