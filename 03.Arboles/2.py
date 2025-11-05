import json
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.fb = 0

    

    

class ArbolAVL:
    def __init__(self):
        self.raiz=None

    def barridoPreorder(self):

        pila = []
        pila.append(self.raiz)

        while pila:
            nodo = pila.pop()
            
            print(nodo.valor,end="  ")

            if nodo.derecha:
                pila.append(nodo.derecha)
            if nodo.izquierda:
                pila.append(nodo.izquierda)
                
        

    def RotarDerecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        
        z.fb = z.fb - 1 - max(0, y.fb)
        y.fb = y.fb - 1 + min(0, z.fb)
        return y

    def RotarIzquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2

        z.fb = z.fb + 1 - min(0, y.fb)
        y.fb = y.fb + 1 + max(0, z.fb)
        return y

    def rebalancear(self, nodo):
        if nodo.fb > 1: 
            if nodo.izquierda.fb >= 0: 
                return self.RotarDerecha(nodo)
            else:
                nodo.izquierda = self.RotarIzquierda(nodo.izquierda)
                return self.RotarDerecha(nodo)
        
        if nodo.fb < -1: 
            if nodo.derecha.fb <= 0:
                return self.RotarIzquierda(nodo)
            else:
                nodo.derecha = self.RotarDerecha(nodo.derecha)
                return self.RotarIzquierda(nodo)
        return nodo

    def insertar(self,val):
        nuevoNodo=NodoAVL(val)

        if not self.raiz:
            self.raiz=nuevoNodo
            return

        camino = [] 
        actual = self.raiz

        while True:
            camino.append(actual)
            if val < actual.valor:
                if not actual.izquierda:
                    actual.izquierda = nuevoNodo
                    break
                else:
                    actual = actual.izquierda
            else:
                if not actual.derecha:
                    actual.derecha = nuevoNodo
                    break
                else:
                    actual = actual.derecha

        alturaCambio = True
        hijo = nuevoNodo 

        while camino and alturaCambio:
            padre = camino.pop()
            
            if hijo == padre.izquierda:
                padre.fb += 1 
            else:
                padre.fb -= 1 
            
            nodoAEnlazar = padre 
            
            if padre.fb == 0:
                alturaCambio = False
            
            elif abs(padre.fb) == 1:
                alturaCambio = True
            
            elif abs(padre.fb) == 2:
                nodoAEnlazar = self.rebalancear(padre)
                alturaCambio = False
            
            if not camino:
                self.raiz = nodoAEnlazar
            else:
                abuelo = camino[-1]
                if abuelo.izquierda == padre: 
                    abuelo.izquierda = nodoAEnlazar
                else:
                    abuelo.derecha = nodoAEnlazar
            
            hijo = nodoAEnlazar

def leer_datos(archivo_json):
    with open(archivo_json, 'r') as f:
        datos = json.load(f) 
    return datos
    

def main():

    arr = leer_datos("datos.json")
    print(arr)
    print(f"Datos a insertar: {arr}")
    
    arbolAVL = ArbolAVL()
    
    for numero in arr:
        arbolAVL.insertar(numero)

    arbolAVL.barridoPreorder()

    

    

if __name__=="__main__":
    main()