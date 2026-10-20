import sys

class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__izquierdo = None
        self.__derecho = None
        self.__altura = 1

    def get_valor(self):
        return self.__valor

    def get_izquierdo(self):
        return self.__izquierdo

    def set_izquierdo(self, nodo):
        self.__izquierdo = nodo

    def get_derecho(self):
        return self.__derecho

    def set_derecho(self, nodo):
        self.__derecho = nodo

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

class ArbolAVL:
    def __init__(self):
        self.__raiz = None

    def insertar(self, valor):
        self.__raiz = self.__insertar_privado(self.__raiz, valor)

    def imprimir_por_niveles(self):
        if not self.__raiz: return
        cola = [self.__raiz]
        while cola:
            nodo = cola.pop(0)
            print(f"{nodo.get_valor()} ", end="")
            if nodo.get_izquierdo(): cola.append(nodo.get_izquierdo())
            if nodo.get_derecho(): cola.append(nodo.get_derecho())
        print()

    def __insertar_privado(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        elif valor < raiz.get_valor():
            raiz.set_izquierdo(self.__insertar_privado(raiz.get_izquierdo(), valor))
        elif valor > raiz.get_valor():
             raiz.set_derecho(self.__insertar_privado(raiz.get_derecho(), valor))
        else:
            return raiz 

        raiz.set_altura(1 + max(self.__obtener_altura(raiz.get_izquierdo()), 
                              self.__obtener_altura(raiz.get_derecho())))

        balance = self.__obtener_balance(raiz)

        if balance > 1 and valor < raiz.get_izquierdo().get_valor():
            print(f"Desbalance en {raiz.get_valor()} tras insertar {valor}. Rotacion Derecha (LL).")
            return self.__rotacion_derecha(raiz)

        if balance < -1 and valor > raiz.get_derecho().get_valor():
            print(f"Desbalance en {raiz.get_valor()} tras insertar {valor}. Rotacion Izquierda (RR).")
            return self.__rotacion_izquierda(raiz)

        if balance > 1 and valor > raiz.get_izquierdo().get_valor():
            print(f"Desbalance en {raiz.get_valor()} tras insertar {valor}. Rotacion Izquierda-Derecha (LR).")
            raiz.set_izquierdo(self.__rotacion_izquierda(raiz.get_izquierdo()))
            return self.__rotacion_derecha(raiz)

        if balance < -1 and valor < raiz.get_derecho().get_valor():
            print(f"Desbalance en {raiz.get_valor()} tras insertar {valor}. Rotacion Derecha-Izquierda (RL).")
            raiz.set_derecho(self.__rotacion_derecha(raiz.get_derecho()))
            return self.__rotacion_izquierda(raiz)

        return raiz

    def __rotacion_izquierda(self, z):
        y = z.get_derecho()
        T2 = y.get_izquierdo()
        
        y.set_izquierdo(z)
        z.set_derecho(T2)
        
        z.set_altura(1 + max(self.__obtener_altura(z.get_izquierdo()), self.__obtener_altura(z.get_derecho())))
        y.set_altura(1 + max(self.__obtener_altura(y.get_izquierdo()), self.__obtener_altura(y.get_derecho())))
        
        return y

    def __rotacion_derecha(self, z):
        y = z.get_izquierdo()
        T3 = y.get_derecho()
        
        y.set_derecho(z)
        z.set_izquierdo(T3)
        
        z.set_altura(1 + max(self.__obtener_altura(z.get_izquierdo()), self.__obtener_altura(z.get_derecho())))
        y.set_altura(1 + max(self.__obtener_altura(y.get_izquierdo()), self.__obtener_altura(y.get_derecho())))
        
        return y

    def __obtener_altura(self, raiz):
        if not raiz: return 0
        return raiz.get_altura()

    def __obtener_balance(self, raiz):
        if not raiz: return 0
        return self.__obtener_altura(raiz.get_izquierdo()) - self.__obtener_altura(raiz.get_derecho())

def main():
    if len(sys.argv) < 2:
        print("Uso: python crear_avl.py <archivo_datos>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    avl = ArbolAVL()

    print(f"--- Leyendo datos de {nombre_archivo} e insertando en AVL ---")
    try:
        archivo = open(nombre_archivo, 'r')
        for linea in archivo:
            if linea.strip(): 
                valor = int(linea.strip())
                print(f"Insertando: {valor}")
                avl.insertar(valor)
        archivo.close()
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {nombre_archivo}")
        sys.exit(1)
    except Exception:
         try:
             archivo = open(nombre_archivo, 'r', encoding='utf-16')
             for linea in archivo:
                 if linea.strip(): 
                     valor = int(linea.strip())
                     print(f"Insertando: {valor}")
                     avl.insertar(valor)
             archivo.close()
         except Exception as e2:
              print(f"Error al leer el archivo: {e2}")
              sys.exit(1)

    print("\n--- Arbol AVL resultante (Barrido por Niveles) ---")
    avl.imprimir_por_niveles()

if __name__ == '__main__':
    main()
