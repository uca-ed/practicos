# INFORMACION REELEVANTE
# https://www.youtube.com/watch?v=zP2xbKerIds&ab_channel=MaanethDeSilva

# CONSIGNA:
#Crear un árbol AVL realizando las inserciones dadas en el archivo de datos.

from collections import deque

class AVL:
    def __init__(self):
        self.root = None
        self.parent = {}  # "Nodo": "Padre"
        self.P = [] # Conjunto de nodos dentro del arbol
        self.E = {} # "Padre" : ["Hijo menor", "Hijo mayor"]
        
    def Height(self, node):
        if node is None:
            return 0

        queue = deque() # cola doble
        queue.append(node)
        height = 0

        while queue:
            l_size = len(queue)
            for _ in range(l_size):
                current = queue.popleft()
                left = self.E[current][0]
                right = self.E[current][1]

                if left is not None:
                    queue.append(left)
                if right is not None:
                    queue.append(right)
            height += 1  # Termina nivel, aumentamos altura

        return height

    
    def Node_Balance(self,node):
        left_height = self.Height(self.E[node][0])
        right_height = self.Height(self.E[node][1])

        return left_height - right_height

    def Insert(self, value):
        self.P.append(value)

        if self.root is None:
            self.root = value
            self.E[value] = [None, None]
            self.parent[self.root] = None
        else:
            # Empiezo con la raíz
            current = self.root
            while True:
                if value < current:
                    # Si voy a la izquierda
                    if self.E[current][0] is None:
                        self.E[current][0] = value
                        self.E[value] = [None, None]
                        self.parent[value] = current
                        break  # Termino la inserción
                    else:
                        # Sigo buscando en la izquierda
                        current = self.E[current][0]
                else:
                    # Si voy a la derecha
                    if self.E[current][1] is None:
                        self.E[current][1] = value
                        self.E[value] = [None, None]
                        self.parent[value] = current
                        break  # Termino la inserción
                    else:
                        # Sigo buscando en la derecha
                        current = self.E[current][1]
        self.Rebalance(value)
    
    def Rebalance(self, node):
        while node is not None:
            balance = self.Node_Balance(node)
            # Desbalance hacia la izquierda (factor de balance > 1)
            # El subárbol izquierdo es más alto que el derecho
            if balance > 1:
                left_child = self.E[node][0]
                # Left Left (el hijo izquierdo también está balanceado o hacia la izquierda)
                if self.Node_Balance(left_child) >= 0:
                    self.Rotate_Right(node)
                # Left Right (el hijo izquierdo está desbalanceado hacia la derecha)
                else:
                    self.Rotate_Left(left_child)
                    self.Rotate_Right(node)
            # Desbalance hacia la derecha (factor de balance < -1)
            # El subárbol derecho es más alto que el izquierdo
            elif balance < -1:
                right_child = self.E[node][1]
                # Right Right (el hijo derecho también está balanceado o hacia la derecha)
                if self.Node_Balance(right_child) <= 0:
                    self.Rotate_Left(node)
                # Right Left (el hijo derecho está desbalanceado hacia la izquierda)
                else:
                    self.Rotate_Right(right_child)
                    self.Rotate_Left(node)
            # Si el nodo está balanceado (factor entre -1 y 1), no se hace nada
            # Se sigue subiendo al padre para revisar si hay más desequilibrios
            node = self.parent[node]


    def Rotate_Right(self,unb):
        # Reasignacion 
        y = self.E[unb][0] # y es el hijo izquierdo de unb
        y_rch = self.E[y][1] # y_rch es el hijo derecho de y
        # Rotación
        self.E[y][1] = unb
        self.E[unb][0] = y_rch
        # Actualizar padres
        parent_unb = self.parent[unb]
        self.parent[y] = parent_unb
        self.parent[unb] = y
        if y_rch is not None:
            self.parent[y_rch] = unb
        # Actualizar el padre de unb para que ahora apunte a y
        if parent_unb is None:
            self.root = y  # y es la nueva raíz
        else:
            # Saber si el nodo sin balancear era hijo izquierdo o derecho
            if self.E[parent_unb][0] == unb:
                self.E[parent_unb][0] = y
            else:
                self.E[parent_unb][1] = y

    def Rotate_Left(self, unb):
        y = self.E[unb][1]       # hijo derecho de z
        y_lch = self.E[y][0]      # hijo izquierdo de y
        # Rotación
        self.E[y][0] = unb
        self.E[unb][1] = y_lch
        # Actualizar padres
        parent_unb = self.parent[unb]
        self.parent[y] = parent_unb
        self.parent[unb] = y
        if y_lch is not None:
            self.parent[y_lch] = unb
        # Actualizar el padre de unb para que apunte a y
        if parent_unb is None:
            self.root = y  # y es la nueva raíz
        else:
            # Saber si el nodo sin balancear era hijo izquierdo o derecho
            if self.E[parent_unb][0] == unb:
                self.E[parent_unb][0] = y
            else:
                self.E[parent_unb][1] = y

def main():
    obj = AVL()
    values = [1,2,3,4,5,6,7,8,9,10]

    for n in values:
        obj.Insert(n)

    print(obj.P)
    print(obj.E)
    #print("altura:", obj.Height(4))

main()