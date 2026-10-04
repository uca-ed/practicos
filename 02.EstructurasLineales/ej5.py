#a,b
#a,c
#asi me imagine el csv

import json
from pathlib import Path
class grafo:
    def init(self):
        self.grafo = {}
        self.grados_entrada = {}
    def inicializar_nodo(self,nodo):
        if nodo not in self.grafo :
            self.grafo[nodo] = []
            self.grados_entrada[nodo] = 0



    def cargarArc(self,archivo):
        origen = ""
        destino = ""
        f= open(archivo) 
        for lineas in f:
            origen, destino = lineas.split(",")
            self.inicializar_nodo(origen)
            self.inicializar_nodo(destino)
            self.grafo[origen].append(destino)
            self.grados_entrada[destino]+=1 


    def t_sort(self):
        res = []
        listos = []

        for nodo in self.grados_entrada:
            if (self.grados_entrada[nodo] == 0):
                listos.append(nodo) # si su grado de entrada  es 0 es el primer nodo
        while (len(listos)!=0):
            aux = listos.pop(0)
            res.append(aux)
            for a in self.grafo[aux]:
                self.grados_entrada[a] -= 1
                if self.grados_entrada[a] == 0:
                    listos.append(a)
        if len(res)!=len(self.grafo):
            raise Exception('el grafo es ciclico')
        else:
            return res