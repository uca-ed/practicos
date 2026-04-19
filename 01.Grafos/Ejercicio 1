import csv
import json

class Grafo:
    def __init__(self, nodos, matriz):
        self.nodos = list(nodos)
        
        # Se copia la matriz
        self.matriz = []
        for fila in matriz:
            self.matriz.append(list(fila))
            
        # Crea un diccionario para saber en qué índice está cada nodo
        self.indice = {}
        for i in range(len(self.nodos)):
            nodo = self.nodos[i]
            self.indice[nodo] = i

    @classmethod
    def desde_csv(cls, ruta):
        matriz = []
        with open(ruta, newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                fila_numeros = []
                for x in fila:
                    # Ignora los espacios en blanco y guarda los números
                    if x.strip() != '':
                        fila_numeros.append(int(x))
                matriz.append(fila_numeros)
        
        # En el CSV los nodos son la posición en la matriz (0, 1, 2...)
        nodos = []
        for i in range(len(matriz)):
            nodos.append(str(i))
            
        return cls(nodos, matriz)

    @classmethod
    def desde_json(cls, ruta):
        with open(ruta) as f:
            data = json.load(f)
        
        nodos = list(data['P'])
        n = len(nodos)
        
        # Arma el diccionario de índices
        indice = {}
        for i in range(n):
            nodo = nodos[i]
            indice[nodo] = i
            
        # Inicia la matriz llena de ceros
        matriz = []
        for i in range(n):
            fila_ceros = [0] * n
            matriz.append(fila_ceros)
            
        # Llena la matriz con las aristas (ponemos un 1 donde hay conexión)
        for origen in data['E']:
            vecinos = data['E'][origen]
            i = indice[origen]  # Busca la fila correspondiente al origen
            
            for v in vecinos:
                j = indice[v]  # Busca la columna correspondiente al destino
                matriz[i][j] = 1
                
        return cls(nodos, matriz)

    def vecindad_derecha(self, nodo):
        """Nodos u tales que (nodo, u) es arista. Es la fila del nodo."""
        i = self.indice[nodo]
        vecinos = []
        
        # Recorre todas las columnas de esa fila
        for j in range(len(self.nodos)):
            # Si hay un 1 y no es un bucle hacia sí mismo, es vecino derecho
            if self.matriz[i][j] == 1 and j != i:
                vecino = self.nodos[j]
                vecinos.append(vecino)
                
        return vecinos

    def vecindad_izquierda(self, nodo):
        """Nodos u tales que (u, nodo) es arista. Es la columna del nodo."""
        j = self.indice[nodo]
        vecinos = []
        
        # Recorre todas las filas de esa columna
        for i in range(len(self.nodos)):
            # Si hay un 1 y no es un bucle hacia sí mismo, es vecino izquierdo
            if self.matriz[i][j] == 1 and i != j:
                vecino = self.nodos[i]
                vecinos.append(vecino)
                
        return vecinos

    def minimales(self):
        """Nodos sin predecesores propios (nadie distinto apunta a ellos)."""
        resultado = []
        for n in self.nodos:
            # Si su vecindad izquierda está vacía, significa que nadie apunta a él
            if len(self.vecindad_izquierda(n)) == 0:
                resultado.append(n)
        return resultado

    def maximales(self):
        """Nodos sin sucesores propios (no apuntan a nadie distinto de si mismos)."""
        resultado = []
        for n in self.nodos:
            # Si su vecindad derecha está vacía, significa que no apunta a nadie
            if len(self.vecindad_derecha(n)) == 0:
                resultado.append(n)
        return resultado

    def mostrar_matriz(self):
        # Validación de seguridad: si el grafo es muy grande, no se imprime
        if len(self.nodos) > 50:
            print(f"El grafo es demasiado grande ({len(self.nodos)} nodos) para mostrar la matriz en consola.")
            return
            
        ancho = 0
        for n in self.nodos:
            if len(str(n)) > ancho:
                ancho = len(str(n))
                
        encabezado = ' ' * (ancho + 2)
        for n in self.nodos:
            encabezado += f'{n:>{ancho}}  '
        print(encabezado)
        
        for i in range(len(self.nodos)):
            n = self.nodos[i]
            fila_str = ""
            for j in range(len(self.nodos)):
                fila_str += f'{self.matriz[i][j]:>{ancho}}  '
            print(f'{n:>{ancho}} | {fila_str}')


if __name__ == '__main__':
    import os
    # Ruta de la carpeta con los archivos
    base = r"C:\Users\boliv\Downloads\archivos_ej1"

    print('\nGrafo desde 01.csv')
    g1 = Grafo.desde_csv(os.path.join(base, '01.csv'))
    g1.mostrar_matriz()
    print(f"Cantidad de minimales: {len(g1.minimales())}")
    print(f"Cantidad de maximales: {len(g1.maximales())}")

    print('\nGrafo desde 02.csv')
    g2 = Grafo.desde_csv(os.path.join(base, '02.csv'))
    g2.mostrar_matriz()
    print(f"Cantidad de minimales: {len(g2.minimales())}")
    print(f"Cantidad de maximales: {len(g2.maximales())}")

    print('\nGrafo desde 03.csv')
    g3 = Grafo.desde_csv(os.path.join(base, '03.csv'))
    g3.mostrar_matriz()
    print(f"Cantidad de minimales: {len(g3.minimales())}")
    print(f"Cantidad de maximales: {len(g3.maximales())}")

    print('\nGrafo desde 04.csv')
    g4 = Grafo.desde_csv(os.path.join(base, '04.csv'))
    g4.mostrar_matriz()
    print('Minimales:', g4.minimales())
    print('Maximales:', g4.maximales())
    print("Vecindad derecha '1':", g4.vecindad_derecha('1'))
    print("Vecindad izquierda '2':", g4.vecindad_izquierda('2'))

    print('\nGrafo desde 01.json')
    g5 = Grafo.desde_json(os.path.join(base, '01.json'))
    print(f"Cantidad de nodos: {len(g5.nodos)}")
    print(f"Vecindad derecha de '1': {g5.vecindad_derecha('1')}")
    print(f"Vecindad izquierda de '1': {g5.vecindad_izquierda('1')}")
    print(f"Cantidad de minimales: {len(g5.minimales())}")
    print(f"Cantidad de maximales: {len(g5.maximales())}")
    print(f"Primeros 10 minimales: {g5.minimales()[:10]}")
    print(f"Primeros 10 maximales: {g5.maximales()[:10]}")
