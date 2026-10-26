
import json
 
 
def leer_csv(nombre_archivo):
    filas = []
    f = open(nombre_archivo)
    for linea in f:
        linea = linea.strip()
        if linea == "":
            continue
        valores = [int(x) for x in linea.split(",")]
        filas.append(valores)
    f.close()
 
    # los nodos se identifican por la posicion que ocupan en la matriz (empezando en 1)
    nodos = [str(i + 1) for i in range(len(filas))]
 
    relaciones = {}
    for i, nodo in enumerate(nodos):
        vecinos = []
        for j, valor in enumerate(filas[i]):
            if valor == 1:
                vecinos.append(nodos[j])
        relaciones[nodo] = vecinos
 
    return nodos, relaciones
 
 
def leer_json(nombre_archivo):
    f = open(nombre_archivo)
    estructura = json.load(f)
    f.close()
    return estructura['P'], estructura['E']
 
 
def leer_grafo(nombre_archivo):
    if nombre_archivo.lower().endswith(".json"):
        return leer_json(nombre_archivo)
    else:
        return leer_csv(nombre_archivo)
 
 
def vecindad_derecha(relaciones, nodo):
    return relaciones.get(nodo, [])
 
 
def vecindad_izquierda(nodos, relaciones, nodo):
    izquierda = []
    for otro in nodos:
        if nodo in relaciones.get(otro, []):
            izquierda.append(otro)
    return izquierda
 
 
def minimales(nodos, relaciones):
    resultado = []
    for nodo in nodos:
        izquierda = vecindad_izquierda(nodos, relaciones, nodo)
        # no cuento al propio nodo, por si la relacion es reflexiva
        tiene_antecesor = any(x != nodo for x in izquierda)
        if not tiene_antecesor:
            resultado.append(nodo)
    return resultado
 
 
def maximales(nodos, relaciones):
    resultado = []
    for nodo in nodos:
        derecha = vecindad_derecha(relaciones, nodo)
        tiene_sucesor = any(x != nodo for x in derecha)
        if not tiene_sucesor:
            resultado.append(nodo)
    return resultado
 
 
def main():
    archivo = input("Archivo del grafo: ")
    nodo = input("Nodo para calcular vecindades: ")
 
    nodos, relaciones = leer_grafo(archivo)
 
    print("Minimales:", minimales(nodos, relaciones))
    print("Maximales:", maximales(nodos, relaciones))
    print(f"Vecindad derecha de {nodo}:", vecindad_derecha(relaciones, nodo))
    print(f"Vecindad izquierda de {nodo}:", vecindad_izquierda(nodos, relaciones, nodo))
 
 
if __name__ == "__main__":
    main()