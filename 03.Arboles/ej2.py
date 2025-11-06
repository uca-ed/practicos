import argparse


class NodoAVL:
    """Nodo de un árbol AVL."""
    
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolAVL:
    """
    Implementación de un árbol AVL (Adelson-Velsky y Landis).
    
    Un árbol AVL es un árbol binario de búsqueda auto-balanceado donde
    la diferencia de alturas entre los subárboles izquierdo y derecho
    de cualquier nodo es como máximo 1.
    """
    
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        """
        Inserta un valor en el árbol AVL manteniendo el balance.
        
        Args:
            valor: valor a insertar
        """
        self.raiz = self._insertar(self.raiz, valor)
    
    def _insertar(self, nodo, valor):
        """
        Función recursiva para insertar un valor.
        
        Args:
            nodo: nodo actual
            valor: valor a insertar
            
        Returns:
            NodoAVL: raíz del subárbol balanceado
        """
        # Paso 1: Inserción normal de BST
        if nodo is None:
            return NodoAVL(valor)
        
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        else:
            # Valor duplicado, no se inserta
            return nodo
        
        # Paso 2: Actualizar altura del nodo ancestro
        nodo.altura = 1 + max(self._obtener_altura(nodo.izq),
                              self._obtener_altura(nodo.der))
        
        # Paso 3: Obtener el factor de balance
        balance = self._obtener_balance(nodo)
        
        # Paso 4: Si el nodo está desbalanceado, hay 4 casos
        
        # Caso Izquierda-Izquierda
        if balance > 1 and valor < nodo.izq.valor:
            return self._rotar_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance < -1 and valor > nodo.der.valor:
            return self._rotar_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        
        return nodo
    
    def _obtener_altura(self, nodo):
        """Retorna la altura de un nodo."""
        if nodo is None:
            return 0
        return nodo.altura
    
    def _obtener_balance(self, nodo):
        """
        Retorna el factor de balance de un nodo.
        Balance = altura(subárbol_izq) - altura(subárbol_der)
        """
        if nodo is None:
            return 0
        return self._obtener_altura(nodo.izq) - self._obtener_altura(nodo.der)
    
    def _rotar_derecha(self, z):
        """
        Rotación simple a la derecha.
        
             z                               y
            / \\                            /   \\
           y   T4    Rotar derecha ->     x     z
          / \\                            / \\   / \\
         x   T3                        T1  T2 T3 T4
        / \\
       T1  T2
        """
        y = z.izq
        T3 = y.der
        
        # Realizar rotación
        y.der = z
        z.izq = T3
        
        # Actualizar alturas
        z.altura = 1 + max(self._obtener_altura(z.izq),
                          self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq),
                          self._obtener_altura(y.der))
        
        # Retornar nueva raíz
        return y
    
    def _rotar_izquierda(self, z):
        """
        Rotación simple a la izquierda.
        
           z                                y
          / \\                             /   \\
        T1   y      Rotar izquierda ->   z     x
            / \\                         / \\   / \\
           T2  x                       T1 T2 T3 T4
              / \\
             T3 T4
        """
        y = z.der
        T2 = y.izq
        
        # Realizar rotación
        y.izq = z
        z.der = T2
        
        # Actualizar alturas
        z.altura = 1 + max(self._obtener_altura(z.izq),
                          self._obtener_altura(z.der))
        y.altura = 1 + max(self._obtener_altura(y.izq),
                          self._obtener_altura(y.der))
        
        # Retornar nueva raíz
        return y
    
    def inorden(self):
        """
        Recorrido in-orden del árbol.
        
        Returns:
            list: valores en orden ascendente
        """
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        """Función auxiliar recursiva para in-orden."""
        if nodo:
            self._inorden(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.der, resultado)
    
    def preorden(self):
        """
        Recorrido pre-orden del árbol.
        
        Returns:
            list: valores en pre-orden
        """
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado
    
    def _preorden(self, nodo, resultado):
        """Función auxiliar recursiva para pre-orden."""
        if nodo:
            resultado.append(nodo.valor)
            self._preorden(nodo.izq, resultado)
            self._preorden(nodo.der, resultado)
    
    def obtener_altura(self):
        """Retorna la altura del árbol."""
        return self._obtener_altura(self.raiz)
    
    def mostrar_arbol(self):
        """Muestra una representación visual del árbol."""
        if self.raiz is None:
            print("Árbol vacío")
            return
        
        lineas = []
        self._construir_representacion(self.raiz, lineas, 0, "R")
        for linea in lineas:
            print(linea)
    
    def _construir_representacion(self, nodo, lineas, nivel, prefijo):
        """
        Construye una representación visual del árbol.
        
        Args:
            nodo: nodo actual
            lineas: lista de strings para construir la representación
            nivel: nivel actual en el árbol
            prefijo: prefijo para identificar el nodo (R=raíz, I=izq, D=der)
        """
        if nodo is None:
            return
        
        indentacion = "    " * nivel
        lineas.append(f"{indentacion}{prefijo}: {nodo.valor} (h={nodo.altura}, b={self._obtener_balance(nodo)})")
        
        if nodo.izq or nodo.der:
            if nodo.izq:
                self._construir_representacion(nodo.izq, lineas, nivel + 1, "I")
            else:
                lineas.append(f"{indentacion}    I: None")
            
            if nodo.der:
                self._construir_representacion(nodo.der, lineas, nivel + 1, "D")
            else:
                lineas.append(f"{indentacion}    D: None")


def cargar_valores_desde_archivo(ruta):
    """
    Carga valores desde un archivo.
    
    El archivo debe contener valores numéricos separados por espacios o saltos de línea.
    
    Args:
        ruta: ruta al archivo
        
    Returns:
        list: lista de valores a insertar
    
    Raises:
        FileNotFoundError: si el archivo no existe
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{ruta}' no fue encontrado")
    
    valores = []
    for token in contenido.split():
        try:
            valores.append(int(token))
        except ValueError:
            try:
                valores.append(float(token))
            except ValueError:
                # Ignorar tokens no numéricos
                pass
    
    return valores


def main():
    parser = argparse.ArgumentParser(
        description='Ejercicio 2 - Árbol AVL con inserciones desde archivo'
    )
    parser.add_argument('archivo', help='Ruta al archivo con valores a insertar')
    parser.add_argument('--mostrar', action='store_true',
                       help='Mostrar estructura del árbol')
    parser.add_argument('--inorden', action='store_true',
                       help='Mostrar recorrido in-orden')
    parser.add_argument('--preorden', action='store_true',
                       help='Mostrar recorrido pre-orden')
    parser.add_argument('--altura', action='store_true',
                       help='Mostrar altura del árbol')
    
    args = parser.parse_args()
    
    # Cargar valores desde archivo
    valores = cargar_valores_desde_archivo(args.archivo)
    
    if not valores:
        print("No se encontraron valores numéricos en el archivo")
        return
    
    # Crear árbol AVL e insertar valores
    arbol = ArbolAVL()
    print(f"Insertando {len(valores)} valores: {valores}")
    print()
    
    for valor in valores:
        arbol.insertar(valor)
    
    hizo_algo = False
    
    if args.mostrar:
        print("Estructura del árbol AVL:")
        print("(h=altura, b=balance)")
        arbol.mostrar_arbol()
        print()
        hizo_algo = True
    
    if args.altura:
        print(f"Altura del árbol: {arbol.obtener_altura()}")
        hizo_algo = True
    
    if args.inorden:
        print(f"Recorrido in-orden: {' '.join(map(str, arbol.inorden()))}")
        hizo_algo = True
    
    if args.preorden:
        print(f"Recorrido pre-orden: {' '.join(map(str, arbol.preorden()))}")
        hizo_algo = True
    
    if not hizo_algo:
        # Por defecto muestra todo
        print("Estructura del árbol AVL:")
        print("(h=altura, b=balance)")
        arbol.mostrar_arbol()
        print()
        print(f"Altura del árbol: {arbol.obtener_altura()}")
        print(f"Recorrido in-orden: {' '.join(map(str, arbol.inorden()))}")
        print(f"Recorrido pre-orden: {' '.join(map(str, arbol.preorden()))}")


if __name__ == '__main__':
    main()
