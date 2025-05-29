# CONSIGNA:
# Dado un arreglo sobre el que está representado un árbol de grado indicado como dato, dar un algoritmo que:
# a) detecte la altura del árbol sin hacer recorridos 
# b) realice un barrido pre-orden

import json
import math

# ASUMO QUE EL ARBOL ES COMPLETO.
# ASUMO QUE EL PRIMER NODO ES LA RAIZ
# Si no es irrelevante el dato de grado del arbol
class Tree:
    def __init__(self,grado):
        self.root = None
        self.grado = grado
        self.P = [] # Conjunto de nodos dentro del arbol
        self.E = {} # "Padre" : ["Hijo menor", "Hijo mayor"]
    
    def Cargar_Json(self, ruta_archivo):
        # Cargamos el JSON
        f = open(ruta_archivo)                       
        estructura = json.load(f)
        f.close()

        # Asigno P y E al objeto de la clase
        self.P = estructura["P"]
        self.E = estructura["E"]

    # Calculo la altura del árbol completo usando el número de nodos y el grado
    # Altura = cantidad de pisos contando el piso de la raiz como cero
    def Get_Height(self):
        N = len(self.P)  
        if N == 0:
            return 0 
        
        # Uso la fórmula de logaritmo para calcular la altura
        height = math.floor(math.log(N, self.grado))
        return height
    
    # Función para barrido pre-orden
    def Pre_Order(self, root):
        result = []
        stack = [root]  # Comienzo con la raíz en el stack
        
        while stack:
            node = stack.pop()  # Extraigo el nodo de la cima del stack
            result.append(node)  # Lo agrego al resultado
            
            # Si el nodo tiene hijos en self.E, los agregamos al stack
            # Los agrego en orden inverso (derecha a izquierda)
            if node in self.E:
                # Apilamos los hijos de derecha a izquierda
                stack.extend(reversed(self.E[node]))
        
        return result
    
def main():
    mi_arbol = Tree(3)
    mi_arbol.Cargar_Json("01.json") 

    altura = mi_arbol.Get_Height()
    print("Altura del árbol:", altura)

    root_node = mi_arbol.P[0]  # Usamos el primer nodo de la lista P como la raíz
    print(mi_arbol.Pre_Order(root_node))


main()