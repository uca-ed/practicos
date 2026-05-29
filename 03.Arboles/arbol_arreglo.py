#arbol_arreglo.py

import math

class ArbolRepresentadoEnArreglo:
    def __init__(self, arreglo, grado):
        self.arreglo = arreglo
        self.grado = grado
        self.n = len(arreglo)

    def obtener_altura_sin_recorrido(self):
        if self.n == 0:
            return 0
        return math.ceil(math.log((self.n * (self.grado - 1)) + 1, self.grado)) - 1

    def barrido_pre_orden(self):
        resultado = []
        self._pre_orden_recursivo(0, resultado)
        return resultado

    def _pre_orden_recursivo(self, indice_actual, resultado):
        if indice_actual >= self.n or self.arreglo[indice_actual] is None:
            return
            
        resultado.append(self.arreglo[indice_actual])
        
        primer_hijo = (self.grado * indice_actual) + 1
        for i in range(self.grado):
            indice_hijo = primer_hijo + i
            self._pre_orden_recursivo(indice_hijo, resultado)