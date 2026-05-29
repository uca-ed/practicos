#estructuras_lineales.py

import os

def procesar_operaciones_cola(ruta_archivo, max_tam=100):
    cola = [None] * max_tam
    frente = 0
    final = 0
    tam = 0
    
    if not os.path.exists(ruta_archivo):
        return
        
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split(",")
            operacion = partes[0].strip()
            
            if operacion == "ENQUEUE":
                if tam != max_tam:
                    valor = partes[1].strip()
                    cola[final] = valor
                    final = (final + 1) % max_tam
                    tam += 1
            elif operacion == "DEQUEUE":
                if tam != 0:
                    valor_extraido = cola[frente]
                    cola[frente] = None  
                    frente = (frente + 1) % max_tam
                    tam -= 1
                    print(f"Extraído (DEQUEUE): {valor_extraido}")
                    
    resultado_final = []
    idx = frente
    for _ in range(tam):
        resultado_final.append(cola[idx])
        idx = (idx + 1) % max_tam
    print(f"Resultado final de la cola: {resultado_final}\n")


def procesar_operaciones_pila(ruta_archivo, max_tam=100):
    pila = [None] * max_tam
    tope = -1
    
    if not os.path.exists(ruta_archivo):
        return
        
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split(",")
            operacion = partes[0].strip()
            
            if operacion == "PUSH":
                if tope != max_tam - 1:
                    valor = partes[1].strip()
                    tope += 1
                    pila[tope] = valor
            elif operacion == "POP":
                if tope != -1:
                    valor_pop = pila[tope]
                    pila[tope] = None
                    tope -= 1
                    print(f"Extraído (POP): {valor_pop}")
                    
    print(f"Resultado final de la pila: {pila[:tope+1]}\n")


class Celda:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def insertar_lista(cabeza, valor_nuevo):
    nuevo = Celda(valor_nuevo)
    if cabeza is None:
        cabeza = nuevo
    else:
        aux = cabeza
        while aux.siguiente is not None:
            aux = aux.siguiente
        aux.siguiente = nuevo
    return cabeza

def mostrar_lista(cabeza):
    elementos = []
    aux = cabeza
    while aux is not None:
        elementos.append(str(aux.valor))
        aux = aux.siguiente
    return " -> ".join(elementos)