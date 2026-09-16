"""
Practica 2 - Estructuras de Datos Lineales
"""

import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(BASE, "datos")


def titulo(n, texto):
    print("\n" + "=" * 78)
    print(f" EJERCICIO {n} - {texto}")
    print("=" * 78 + "\n")


def ej1():
    import ej1_cola
    titulo(1, "Colas sobre un arreglo")
    ej1_cola.ejecutar(os.path.join(DATOS, "operaciones_cola.txt"))


def ej2():
    import ej2_pila
    titulo(2, "Pilas sobre un arreglo")
    ej2_pila.ejecutar(os.path.join(DATOS, "operaciones_pila.txt"))


def ej3():
    import ej3_lista
    titulo(3, "Listas con celdas de enlace simple")
    ej3_lista.demo()


def ej4():
    import ej4_radix
    titulo(4, "Radix Sort")
    ej4_radix.ejecutar(os.path.join(DATOS, "alfabetos.txt"),
                       os.path.join(DATOS, "palabras.txt"))


def ej5():
    import ej5_tsort
    titulo(5, "T-Sort sobre un grafo leido de disco")
    print(">>> CASO A: grafo aciclico\n")
    ej5_tsort.ejecutar(os.path.join(DATOS, "grafo.txt"))
    print("\n\n>>> CASO B: grafo con ciclo\n")
    ej5_tsort.ejecutar(os.path.join(DATOS, "grafo_ciclico.txt"))


def ej6():
    import ej6_arreglo5d
    titulo(6, "Arreglos de 5 dimensiones sobre arreglos lineales")
    ej6_arreglo5d.ejecutar(bloque=40, edificio=2, piso=3)


def ej7():
    titulo(7, "Sort topologico sobre un grafo dado en un archivo")
    print("Este punto es el mismo algoritmo que el ejercicio 5.")
    print("Se resuelve en ej5_tsort.py, que ya lee el grafo desde disco")
    print("y devuelve la secuencia t-sort (o avisa si la estructura es ciclica).\n")
    ej5()


EJERCICIOS = {1: ej1, 2: ej2, 3: ej3, 4: ej4, 5: ej5, 6: ej6, 7: ej7}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        if n not in EJERCICIOS:
            print(f"No existe el ejercicio {n}. Elegi entre 1 y 7.")
            sys.exit(1)
        EJERCICIOS[n]()
    else:
        # el 7 es el mismo algoritmo que el 5, no lo repito al correr todos
        for n in [1, 2, 3, 4, 5, 6]:
            EJERCICIOS[n]()
        print("\n" + "=" * 78)
        print(" Todos los ejercicios corrieron sin errores.")
        print(" (el punto 7 es el mismo algoritmo que el 5: python3 main.py 7)")
        print("=" * 78)
