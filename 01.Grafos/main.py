
from lectura_grafos import leer_json_a_relaciones
from grafos_utils import *

# ------------------ EJERCICIO 1 ------------------

print("\n" + "="*20 + " EJERCICIO 1 " + "="*20)
relaciones_ej1 = leer_json_a_relaciones("archivos_ej1/01.json")
nodos_ej1 = obtener_nodos(relaciones_ej1)

print("Vecindades:")
for nodo in nodos_ej1:
    print(f"{nodo}: derecha={vecindad_derecha(nodo, relaciones_ej1)}, izquierda={vecindad_izquierda(nodo, relaciones_ej1)}")

minimos, maximos = minimos_maximos(relaciones_ej1)
print(f"Mínimos: {minimos}")
print(f"Máximos: {maximos}")
print("Matriz de adyacencia:")
for fila in matriz_adyacencia(relaciones_ej1, nodos_ej1):
    print(fila)


# ------------------ EJERCICIO 2 ------------------

print("\n" + "="*20 + " EJERCICIO 2 " + "="*20)
archivos_ej2 = ["01.json", "02.json", "03.json"]
for nombre_archivo in archivos_ej2:
    path = f"archivos_ej2/{nombre_archivo}"
    relaciones = leer_json_a_relaciones(path)
    nodos = obtener_nodos(relaciones)
    print(f"\nArchivo: {nombre_archivo}")
    print(f"Reflexivo: {es_reflexivo(relaciones, nodos)}")
    print(f"Simétrico: {es_simetrico(relaciones)}")
    print(f"Antisimétrico: {es_antisimetrico(relaciones)}")
    print(f"Transitivo: {es_transitivo(relaciones)}")
    print(f"Tipo de relación: {tipo_relacion(relaciones)}")


# ------------------ EJERCICIO 3 ------------------

print("\n" + "="*20 + " EJERCICIO 3 " + "="*20)
archivos_ej3 = [
    "esDivisorDe-200.json",
    "esDivisorDe-2000.json",
    "esDivisorDe-20000.json"
]

for archivo in archivos_ej3:
    relaciones = leer_json_a_relaciones(f"archivos_ej3/{archivo}")
    nodos = obtener_nodos(relaciones)
    if len(nodos) < 2:
        continue
    origen, destino = nodos[0], nodos[-1]
    camino = encontrar_camino(origen, destino, relaciones)
    print(f"Archivo: {archivo}")
    print(f"Camino de {origen} a {destino}: {camino if camino else 'No hay camino'}")
