import Main

#EJERCICIO 2
#A tener en cuenta: json 3 tarda en cargar porque son muchos nodos y relaciones, pero no es un error

def obtener_relaciones(datos):
    relaciones = set()
    for origen, destinos in datos["E"].items():
        for destino in destinos:
            relaciones.add((origen, destino))
    return relaciones

def es_reflexivo(nodos, relaciones):
    return all((nodo, nodo) in relaciones for nodo in nodos)

def es_simetrico(relaciones):
    return all((y, x) in relaciones for (x, y) in relaciones)

def es_antisimetrico(relaciones):
    return all(x == y or (y, x) not in relaciones for (x, y) in relaciones)

def es_transitivo(relaciones):
    mapa_relaciones = {}
    for (x, y) in relaciones:
        if x not in mapa_relaciones:
            mapa_relaciones[x] = set()
        mapa_relaciones[x].add(y)
    for (x, y) in relaciones:
        if y in mapa_relaciones:
            for z in mapa_relaciones[y]:
                if (x, z) not in relaciones:
                    return False
    return True


#Se debe ingresar el nombre del archivo. 
#por ejemplo: 'x.json'
def main_2(arch):
    print("Archivo: ", arch)
    datos = Main.cargar_json("archivos_ej2/" + arch)
    nodos = set(datos["P"])
    relaciones = obtener_relaciones(datos)

    propiedades = {
        "Reflexiva": es_reflexivo(nodos, relaciones),
        "Simétrica": es_simetrico(relaciones),
        "Antisimétrica": es_antisimetrico(relaciones),
        "Transitiva": es_transitivo(relaciones)
    }

    if propiedades["Reflexiva"] and propiedades["Simétrica"] and propiedades["Transitiva"]:
        tipo_relacion = "Relación de equivalencia"
    elif propiedades["Reflexiva"] and propiedades["Antisimétrica"] and propiedades["Transitiva"]:
        tipo_relacion = "Orden parcial"
    else:
        tipo_relacion = "Ninguna"

    for propiedad, valor in propiedades.items():
        print(f" - {propiedad}: {'Sí' if valor else 'No'}")
    print(f"=> Tipo de relación: {tipo_relacion}\n")

main_2('01.json')