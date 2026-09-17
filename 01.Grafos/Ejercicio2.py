import json

#Ejercicio 2
#Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

def leerArchivo_json(nomarch):
    f = open(nomarch)
    estructura = json.load(f)
    f.close()
    return estructura

def reflexividad(struct):
    reflexivo=True
    for i in struct['E']:
        if not (i in struct['E'][i]):
            reflexivo=False
    return reflexivo

def simetria(struct):
    simetria=True
    for i in struct['E']:
        for j in struct['E'][i]:
            if not(i in struct['E'][j]):
                simetria=False
    return simetria

def antisimetriaDebil(struct):
    antisimetriaDebil=True
    for i in struct['E']:
        for j in struct['E'][i]:
            if not((not(i in struct['E'][j])) or (i==j)):
                antisimetriaDebil=False
    return antisimetriaDebil

def transitividad(struct):
    transitivo=True
    for i in struct['E']:
        for j in struct['E'][i]:
            for k in struct['E'][j]:
                if not(k in struct['E'][i]):
                    transitivo=False
    return transitivo

def ordenParcial(struct):
    return (antisimetriaDebil(struct) and transitividad(struct))

def equivalencia(struct):
    return (reflexividad(struct) and simetria(struct) and transitividad(struct))

def main():
    struct=leerArchivo_json("01.json")
    print("¿el grafo es un orden?:",ordenParcial(struct))
    print("¿el grafo tiene relacion de equivalencia?:",equivalencia(struct))

main()
