
"""
lectura_grafos.py

Este módulo se encarga de la carga de grafos desde archivos CSV y JSON. Convierte
estas representaciones a listas de relaciones (pares de nodos), que pueden ser
utilizadas por las funciones del módulo grafos_utils.
"""

import csv
import json
from typing import List, Tuple

def leer_csv_a_relaciones(path: str) -> List[Tuple[str, str]]:
    """
    Lee un archivo CSV con dos columnas y devuelve una lista de relaciones (pares).
    """
    relaciones = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            if len(fila) >= 2:
                relaciones.append((fila[0].strip(), fila[1].strip()))
    return relaciones

def leer_json_a_relaciones(path: str) -> List[Tuple[str, str]]:
    """
    Lee un archivo JSON con formato {'E': {'a': ['b', 'c']}} y devuelve una lista de relaciones.
    """
    relaciones = []
    with open(path, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        if 'E' in datos:
            for origen, destinos in datos['E'].items():
                for destino in destinos:
                    relaciones.append((origen.strip(), destino.strip()))
    return relaciones

def leer_matriz_csv(path: str) -> List[List[int]]:
    """
    Lee una matriz de adyacencia desde un CSV y la devuelve como lista de listas de enteros.
    """
    matriz = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            if fila:
                matriz.append([int(x) for x in fila])
    return matriz
