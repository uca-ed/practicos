# -*- coding: utf-8 -*-
"""
Consigna 2 — Árbol AVL
Utilizo el archivo 02.json de la sengunda carpeta de datos:
- Insertar los valores (lista "P") en un árbol AVL en ese mismo orden.
- Mostrar recorridos y altura final.
"""

import json

# Definición de nodo AVL
class NodoAVL:
    __slots__ = ("valor", "izq", "der", "altura")
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        # Por convención, un nodo aislado tiene altura 1
        self.altura = 1

# Funciones auxiliares del AVL
# 
# altura devuelve la altura almacenada en el nodo (0 si es None)
def altura(nodo):
    return nodo.altura if nodo else 0

#Recalcula la altura del nodo en base a sus hijos.
def actualizar_altura(nodo):
    nodo.altura = max(altura(nodo.izq), altura(nodo.der)) + 1

#diferencia de alturas entre subárbol izquierdo y derecho
def factor_balance(nodo):
    return (altura(nodo.izq) - altura(nodo.der)) if nodo else 0

# Rotaciones
def rotar_derecha(y):
    """Rotación simple a la derecha (caso Izquierda–Izquierda)."""
    x = y.izq
    t2 = x.der
    # Rotación
    x.der = y
    y.izq = t2
    # Actualizar alturas
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rotar_izquierda(x):
    """Rotación simple a la izquierda (caso Derecha–Derecha)."""
    y = x.der
    t2 = y.izq
    # Rotación
    y.izq = x
    x.der = t2
    # Actualizar alturas
    actualizar_altura(x)
    actualizar_altura(y)
    return y

# Inserción con balanceo es decir Inserta 'valor' en el subárbol con raíz 'nodo' manteniendo propiedad AVL.
# devuelve la nueva raiz del subarbol
def insertar(nodo, valor):
    # Inserción BST estándar, BST es binary search tree
    if nodo is None:
        return NodoAVL(valor)
    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    elif valor > nodo.valor:
        nodo.der = insertar(nodo.der, valor)
    else:
        # Si el valor ya existe, no insertamos duplicado.
        return nodo

    # Actualizar altura del nodo actual
    actualizar_altura(nodo)

    # Calcular factor de balance para decidir rotación
    fb = factor_balance(nodo)

    # 4 casos típicos del AVL:
    # 1) Izquierda–Izquierda
    if fb > 1 and valor < nodo.izq.valor:
        return rotar_derecha(nodo)

    # 2) Derecha–Derecha
    if fb < -1 and valor > nodo.der.valor:
        return rotar_izquierda(nodo)

    # 3) Izquierda–Derecha
    if fb > 1 and valor > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)

    # 4) Derecha–Izquierda
    if fb < -1 and valor < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    # Si no hizo falta rotar, devolvemos tal cual
    return nodo

# Recorridos
def en_orden(nodo, salida):
    """Izquierda - Nodo - Derecha (debe quedar ordenado)."""
    if not nodo:
        return
    en_orden(nodo.izq, salida)
    salida.append(nodo.valor)
    en_orden(nodo.der, salida)

def pre_orden(nodo, salida):
    """Nodo - Izquierda - Derecha."""
    if not nodo:
        return
    salida.append(nodo.valor)
    pre_orden(nodo.izq, salida)
    pre_orden(nodo.der, salida)

def post_orden(nodo, salida):
    """Izquierda - Derecha - Nodo."""
    if not nodo:
        return
    post_orden(nodo.izq, salida)
    post_orden(nodo.der, salida)
    salida.append(nodo.valor)

# Programa principal
def main():
    # Leer datos
    with open("C:/Users/feder/OneDrive/Documentos/GitHub/practicos/03.Arboles/archivos_ej2/01.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

    # Inserciones (convertimos a enteros)
    inserciones = [int(x) for x in datos.get("P", [])]

    # Construir el AVL
    raiz = None
    for v in inserciones:
        raiz = insertar(raiz, v)

    # Altura final (ya está almacenada en el nodo raíz)
    altura_final = altura(raiz)

    # Recorridos
    lista_en_orden = []
    lista_pre_orden = []
    lista_post_orden = []
    en_orden(raiz, lista_en_orden)
    pre_orden(raiz, lista_pre_orden)
    post_orden(raiz, lista_post_orden)

    # Mostrar resultados
    print("=== CONSIGNA 2 — AVL ===")
    print(f"Cantidad de inserciones: {len(inserciones)}")
    print(f"Altura final del AVL: {altura_final}")
    # limito la salida ya que sino queda re desprolijo, pero se entiende la idea.
    print("Recorrido EN-ORDEN  :", lista_en_orden[:120], "..." if len(lista_en_orden) > 120 else "")
    print("Recorrido PRE-ORDEN :", lista_pre_orden[:120], "..." if len(lista_pre_orden) > 120 else "")
    print("Recorrido POST-ORDEN:", lista_post_orden[:120], "..." if len(lista_post_orden) > 120 else "")

if __name__ == "__main__":
    main()
