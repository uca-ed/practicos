import json

def es_reflexiva(estructura):
    count=0
    for x in estructura['P']:
        if x in estructura['E'][x] and x in estructura['E']:
            count+=1
    if count == len(estructura['P']):
        print("es reflexiva")
        return True
    else:
        print("no es reflexiva")
        return False

def es_reflexiva_gonza(estructura):
    count=0
    for x in estructura['P']:
        if not(x in estructura['E'][x] and x in estructura['E']):
            print("No es reflexiva")
            return False
    print("Es reflexiva")
    return True;    
            

def es_Simetrica(estructura):
    for x in estructura['P']:
        for y in estructura['E'][x]:
            if x not in estructura['E'][y] and y in estructura['E']:
                print("no es simetrica")
                return False
    print("es simetrica")
    return True
            



def es_antisimetrica(estructura):
    es_antisimetrica = True

    for x in estructura['E']:
        for y in estructura['E'][x]:
            # Solo comprobamos para elementos distintos (x != y)
            if x != y:
                # Si 'y' se relaciona de vuelta con 'x', rompe la antisimetría
                if y in estructura['E'] and x in estructura['E'][y]:
                    es_antisimetrica = False
                    break
                    
        if not es_antisimetrica:
            break  # Cortamos el bucle exterior

    if es_antisimetrica:
        print("es antisimétrica")
    else:
        print("no es antisimétrica")

def es_transitiva(estructura):
    es_transitiva = True

    for x in estructura['E']:
        for y in estructura['E'][x]:
            # Si 'y' tiene vecinos hacia otros nodos ('z')
            if y in estructura['E']:
                for z in estructura['E'][y]:
                    # Verificamos si la conexión directa 'x -> z' NO existe
                    if z not in estructura['E'][x]:
                        es_transitiva = False
                        break
                        
            if not es_transitiva:
                break
                
        if not es_transitiva:
            break  # Cortamos el bucle exterior

    if es_transitiva:
        print("es transitiva")
    else:
        print("no es transitiva")

def main():
    f = open('archivosEjemplos/archivos_ej2/01.json')
    estructura = json.load(f)

    print(" ")
    print(" ")
    es_reflexiva(estructura)
    print(" ")
    print(" ")
    es_Simetrica(estructura)
    print(" ")
    print(" ")
    es_antisimetrica(estructura)
    print(" ")
    print(" ")
    es_transitiva(estructura)

    

    f.close()

main()