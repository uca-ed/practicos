#Librerias necesarias
import json
import csv

# -------- FUNCIONES -------- #

def cargar_json(ruta_archivo):
    f = open(ruta_archivo)                       
    estructura = json.load(f)
    f.close()
    return estructura 


def leer_matriz_csv(ruta_archivo):
    matriz = []
    with open(ruta_archivo, newline='') as f:
        lector = csv.reader(f)
        for fila in lector:
            fila = [int(x) for x in fila]
            matriz.append(fila)
    return matriz

def identificar_archivo(archivo):
    # Obtenemos la extensión del archivo
    extension = archivo.split('.')[-1].lower()

    # Comprobamos si es CSV o JSON
    if extension == 'csv':
        return 'csv'
    elif extension == 'json':
        return 'json'
    else:
        raise ValueError(f"El archivo {archivo} no tiene una extensión válida (debe ser .csv o .json)")

