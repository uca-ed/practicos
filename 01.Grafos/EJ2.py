import json
f = open('archivos_ej2/01.json') #CAMBIAR ACORDE AL ARCHIVO A ANALIZAR!
estructura = json.load(f)
def esReflexiva(estructura):
    for i in estructura['E']:
        if i not in estructura['E'][i]:
            return False
    return True

def esSimetrica(estructura):
    for k in estructura['E']:
        for v in estructura['E'][k]:
            if k not in estructura['E'][v]:
                return False
    return True

def esTransitiva(estructura):
    for k in estructura['E']:
        for v in estructura['E'][k]:
            for w in estructura['E'][v]:
                if w not in estructura['E'][k]:
                    return False
    return True

def esAntisimetrica(estructura):
    for k in estructura['E']:
        for v in estructura['E'][k]:
            if k != v and k in estructura['E'][v]:
                return False
    return True
reflexiva = esReflexiva(estructura)
simetrica = esSimetrica(estructura)
antisimetrica = esAntisimetrica(estructura)
transitiva = esTransitiva(estructura)
print("\nReflexiva: ", reflexiva)
print("\nSimétrica: ", simetrica)
print("\nAntisimétrica: ", antisimetrica)
print("\nTransitiva: ", transitiva)
if reflexiva and simetrica and transitiva:
    print("\nEs una relación de equivalencia")
elif reflexiva and antisimetrica and transitiva:
    print("\nEs una relación de orden")
else:
    print("\nNo cumple con las propiedades de una relación de equivalencia ni de orden")    
f.close()
