import json

def leer_json(archivo):
    f = open(archivo)
    estructura = json.load(f)
    reflexivo=True
    simetrico=True
    antisimetrico=True
    transitivo=True
    comparable=True

    #Verifico la reflexividad
    for nodo_origen, nodos_destino in estructura['E'].items():
        if nodo_origen not in nodos_destino:
            reflexivo=False
    
    #Verifico la simetria y antisimetria
    for nodo_origen, nodos_destino in estructura['E'].items():
        for vecino in nodos_destino:
            if nodo_origen not in estructura['E'].get(vecino,[]):
                simetrico=False
            else:
                antisimetrico=False
    
    #Verifico la transitividad
    for nodo in estructura['E']:
        if transitivo==False:
            break
        for vecino in estructura['E'][nodo]:
            if transitivo==False:
                break
            for vecino_lejano in estructura['E'][vecino]:
                if vecino_lejano not in estructura['E'][nodo]:
                    transitivo=False
                    break
    
    #Verifico la comparabilidad para determinar si el grafo es un orden total
    for i in range(len(estructura['P'])):
        if comparable==False:
            break
        for j in range(i+1, len(estructura['P'])):
            a=estructura['P'][i]
            b=estructura['P'][j]
            relacion_ab= b in estructura['E'].get(a,[])
            relacion_ba= a in estructura['E'].get(b,[])
            if not(relacion_ab or relacion_ba):
                comparable=False
                break
    print("Propiedades del grafo: ")
    print("Reflexivo:",reflexivo)
    print("Simetrico:",simetrico)
    print("Antisimetrico:",antisimetrico)
    print("Transitivo:",transitivo)
    if reflexivo and antisimetrico and transitivo:
        if comparable:
            print("El grafo es un orden total")
        else:
            print("El grafo es un orden parcial")
    elif reflexivo and simetrico and transitivo:
        print("El grafo es una relacion de equivalencia")
    else:
        print("El grafo no es ningun tipo de orden ni relacion de equivalencia")

def main():
    archivo="01.json"
    leer_json(archivo)
main()