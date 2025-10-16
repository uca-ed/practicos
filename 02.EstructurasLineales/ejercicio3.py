class Nodo:
    def __init__(self, dato):
        self.dato  = dato
        self.siguiente = None


class ListaEnlazada: 

    def __init__(self):
        self.primero = None
        self.longitud = 0


    def estaVacia(self):
        return self.primero is None

    def insertarInicio(self,dato):
         nuevo = Nodo(dato)
         nuevo.siguiente = self.primero
         self.primero = nuevo
         self.longitud +=1

    
    def insertar(self,dato): 
        nuevo = Nodo(dato)
        if self.estaVacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.longitud +=1

    def eliminarFiltrado(self, dato): 
        actual = self.primero
        anterior = None

        while actual: 
            if actual.dato == dato:
                if anterior is None:
                    self.primero = actual.siguiente
                
                else: 
                    anterior.siguiente = actual.siguiente
                self.longitud -=1
                return True
            anterior = actual
            actual = actual.siguiente

        return False
    
    def mostrar(self):
        actual = self.primero
        if self.estaVacia():
            print("Vacia")
            return
        print("Contenido de la lista ")
        while actual:
            print(f"{actual.dato}", end= "-->")
            actual=actual.siguiente

    def buscar(self,dato):
        actual = self.primero
        while actual:
            if actual.dato == dato: 
                return True
            actual = actual.siguiente
        return False
    
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar(10)
    lista.insertar(20)
    lista.insertarInicio(5)
    lista.insertar(30)
    lista.mostrar()
    print("\nEliminando 20...")
    lista.eliminarFiltrado(20)
    lista.mostrar()
    print("\n¿Está el 30?", lista.buscar(30))
    print("¿Está el 100?", lista.buscar(100))
