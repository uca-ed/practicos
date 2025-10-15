import csv

class ColaTamañoFijo:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.arreglo = [None] * tamaño
        self.inicio = 0
        self.fin = 0
        
    def imprimir(self): # es hacer trampa
        print(self.arreglo)

    def encolar(self, valor):
        if self.arreglo[self.inicio] != None:
            return -1 # No se puede encolar si la cola está llena, pero tampoco hace falta un error
        self.arreglo[self.inicio] = valor
        self.inicio += 1
        if self.inicio >= self.tamaño :
            self.inicio = 0
        return 0 # Se coló correctamente
        

    def desencolar(self):
        if self.arreglo[self.fin] == None:
            raise Exception("La cola está vacía") # No se puede desencolar de una cola vacía
        valor = self.arreglo[self.fin]
        self.arreglo[self.fin] = None
        self.fin += 1
        if self.fin >= self.tamaño :
            self.fin = 0
        return valor
    

def main():
    with open('datos_cola.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        datos = list(lector_csv) # una lista de python con 
        print(f"Utilizo los valores de la siguiente lista:")
        for dato in datos:
            print(dato)

        animales = ColaTamañoFijo(5)

        print("\nEjercicio 1 : Cola sobre arreglo\n")


        print("\nEncolo valores (0: encolado | -1: cola llena): ")
        print(animales.encolar(datos.pop(0)[0]))  #  0
        print(animales.encolar(datos.pop(0)[0]))  #  0
        print(animales.encolar(datos.pop(0)[0]))  #  0
        print(animales.encolar(datos.pop(0)[0]))  #  0
        print(animales.encolar(datos.pop(0)[0]))  #  0
        print(animales.encolar(datos.pop(0)[0]))  # -1

        print("\nValores dentro de la cola: ")
        animales.imprimir() # es trampa -> ['Perro', 'Pato', 'Ganzo', 'Lobo', 'Rana']
        print()

        print("\nDesencolo algunos valores: ")
        print(animales.desencolar()) # Perro
        print(animales.desencolar()) # Pato 

        print("\nValores dentro de la cola: ")
        animales.imprimir() # es trampa -> [None, None, 'Ganzo', 'Lobo', 'Rana']
        print()

        print("\nEncolo algunos valores: ")
        print(animales.encolar(datos.pop(0)[0])) #  0
        print(animales.encolar(datos.pop(0)[0])) #  0
        print(animales.encolar(datos.pop(0)[0])) # -1

        print("\nValores dentro de la cola: ")
        animales.imprimir() # es trampa -> ['Rana', 'Mono', 'Ganzo', 'Lobo', 'Rana']
        print()

        print("\nDesencolo algunos valores: ")
        print(animales.desencolar()) # Ganzo
        print(animales.desencolar()) # Lobo
        print(animales.desencolar()) # Rana
        print(animales.desencolar()) # Rana
        print(animales.desencolar()) # Mono

        print("\nLa cola ha quedado vacía: ")
        animales.imprimir() # es trampa --> [None, None, None, None, None]

        print("\nIntento desencolar de una cola vacía")
        try:
            print(animales.desencolar()) # desencolar de una cola vacía tira error

        except Exception as e:
            print(f"\nHay un error: {e}") # -> La cola está vacía


main()
print()


