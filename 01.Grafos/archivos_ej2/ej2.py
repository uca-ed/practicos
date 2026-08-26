import json
from pathlib import Path

class grafo:
    def __init__(self):
        self.nodo = []
        self.matriz = []

    def vecindadDer(self,nodo):
            n = len(self.matriz)
            vecindadDer=[]#si recorro de fila a columna estoy viendo de donde salen las flechas de i, osea que veos sus vecinos derechos
            for j in range(n):
            #p(i,j)
                if (self.matriz[nodo][j] == 1):
                    vecindadDer.append(j)
            return vecindadDer
            
            
    def vecindadIzq(self,nodo):
        n = len(self.matriz)
        vecindadIzq=[]#si recorro de fila a columna estoy viendo de donde salen las flechas de i, osea que veos sus vecinos derechos
        for j in range(n):
        #p(i,j)
            if(self.matriz[j][nodo] == 1):                  
                vecindadIzq.append(j)
        return vecindadIzq

    def cargar_archivo(self, ruta_archivo):
                if ruta_archivo.endswith('.csv'):
                    self.cargar_csv(ruta_archivo)
                elif ruta_archivo.endswith('.json'):
                    self.cargar_json(ruta_archivo)
    def cargar_csv(self,archivo):
        j=0
        f = open(archivo)
        for filas in f:
            linea = filas.strip()
            valores = linea.split(",")
            ls_def =[]
            for i in valores:
                
                ls_def.append(int(i))
            self.matriz.append(ls_def)
            n = len(self.matriz) #filas = cantidad de nodos 
        while (j<n):
            self.nodo.append(j)
            j+=1
        f.close()
        
    def cargar_json(self,archivo):
        f = open(archivo)
        estructura = json.load(f)
        self.nodo = estructura["P"]
        arcos = estructura["E"]
        for n in self.nodo:
            fila = [0] * len(self.nodo)
            for vecino in arcos[n]:
                j=self.nodo.index(vecino) #si esta dentro significa que va con bit encendido
                fila[j] = 1
            self.matriz.append(fila)
        f.close()

    def buscarMinimo(self):
        minimo = []
        for i in range(len(self.matriz)):
            comprobante = self.vecindadIzq(i)
            if comprobante==[]:
                minimo.append(i)
        return minimo
                  
    def buscarMaximo(self):
        Max=[]
        for i in range(len(self.matriz)):
            comprobante = self.vecindadDer(i)
            if comprobante == []:
                Max.append(i)
        return Max
                
    #minimos columna de 0
    #maximos fila de 0

if __name__ == "__main__":
        print("--- INICIANDO PRUEBAS DEL GRAFO ---")

        # Creamos nuestro objeto Grafo
        mi_grafo = grafo()

        # Vamos a probar cargar el CSV de la cátedra
        # Asegurate de que la ruta sea correcta si el archivo está en la carpeta archivos_ej1
        ruta_json = Path(__file__).parent / "01.json"
        mi_grafo.cargar_archivo(str(ruta_json))

        print("\n1. Nodos cargados:", mi_grafo.nodo)
        print("2. Matriz cargada:")
        for fila in mi_grafo.matriz:
            print(fila)

        print("\n--- PRUEBA DE OPERADORES ---")
        # Si probamos con el nodo 0
        print("Vecindad Derecha del nodo 0:", mi_grafo.vecindadDer(0))
        print("Vecindad Izquierda del nodo 0:", mi_grafo.vecindadIzq(0))

        print("\n--- PRUEBA DE EXTREMOS ---")
        print("Minimales del grafo:", mi_grafo.buscarMinimo())
        print("Maximales del grafo:", mi_grafo.buscarMaximo())