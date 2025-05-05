#---------------------Es Isomorfa
def checkSiTienenMismaCantidadDeBucles(grafo1, grafo2):
    cant1=0
    cant2=0
    for key1 in (grafo1.keys()):
        if (key1==grafo1.get(key1)):
            cant1=cant1+1
    for key2 in (grafo2.keys()):
        if (key2==grafo2.get(key2)):
            cant2=cant2+1
    if (cant1==cant2):
        return True
    else:
        return False    

def checkSiTienenMismaCantidadDeNodos(grafo1, grafo2):
    cant1=0
    cant2=0
    for key1 in (grafo1.keys()):
        cant1=cant1+1
    for key2 in (grafo2.keys()):
        cant2=cant2+1
    if (cant1==cant2):
        return True
    else:
        return False

def verIso(grafo1, grafo2):
    continuar = checkSiTienenMismaCantidadDeNodos(grafo1, grafo2)
    bucles = checkSiTienenMismaCantidadDeBucles(grafo1, grafo2)
    if (continuar == False) or (bucles == False):
        print("No son iso")
        return 0
    grafAux = grafo1.copy()
    for key1 in (grafo1.keys()):
        grado1 = (len(grafo1.get(key1)))
        for key2 in (grafo2.keys()):
            grado2= (len(grafo2.get(key2)))
            if (grado1 == grado2):
                grafo2.pop(key2)
                break            
    if (grafo2 == {}):
        print("Son iso")
    else:
        print("No son iso")
    return 0

grafo1 = {
    'A':['E','I'],
    'E':['I','A'],
    'I':['O'],
    'O':['A']
    }

grafo2 = {
    'A':['E','I'],
    'O':['A'],
    'E':['I','A'],
    'I':['O']
    }

verIso(grafo1, grafo2)
grafo3 = {
    'A':['E','I'],
    'E':['I','A'],
    'I':['O']
    }
verIso(grafo1, grafo3)