import csv

class PilaTamañoFijo:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.arreglo = [None] * tamaño
        self.tope = 0
        
    def imprimir(self): # es hacer trampa
        print(self.arreglo)

    def push(self, valor):
        if self.tope >= self.tamaño:
            return -1 # No se puede pushear si la pila está llena, pero tampoco hace falta un error
        self.arreglo[self.tope] = valor
        self.tope += 1
        return 0 # Se pusheó correctamente
        

    def pop(self):
        self.tope -= 1
        if self.tope < 0:
            raise Exception("La pila está vacía") # No se puede popear una pila vacía
        valor = self.arreglo[self.tope]
        self.arreglo[self.tope] = None # No hace falta pero queda más lindo al hacer trampa
        return valor
    
def main():
    with open('datos_cola.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        datos = list(lector_csv) # una lista de python con 
        print(f"Utilizo los valores de la siguiente lista:")
        for dato in datos:
            print(dato) 

        animales = PilaTamañoFijo(5)

        print("\nEjercicio 2 : Pila sobre arreglo\n")

        print("\nPusheo valores (0: pusheado | -1: pila llena): ")
        print(animales.push(datos.pop(0)[0]))  #  0
        print(animales.push(datos.pop(0)[0]))  #  0
        print(animales.push(datos.pop(0)[0]))  #  0
        print(animales.push(datos.pop(0)[0]))  #  0
        print(animales.push(datos.pop(0)[0]))  #  0
        print(animales.push(datos.pop(0)[0]))  # -1

        print("\nValores dentro de la pila: ")
        animales.imprimir() # es trampa -> ['Perro', 'Pato', 'Ganzo', 'Lobo', 'Rana']
        print()

        print("\nPopeo algunos valores: ")
        print(animales.pop()) # Rana
        print(animales.pop()) # Lobo 

        print("\nValores dentro de la pila: ")
        animales.imprimir() # es trampa -> ['Perro', 'Pato', 'Ganzo', None , None]
        print()

        print("\nPusheo valores")
        print(animales.push(datos.pop(0)[0])) #  0
        print(animales.push(datos.pop(0)[0])) #  0
        print(animales.push(datos.pop(0)[0])) # -1

        print("\nValores dentro de la pila: ")
        animales.imprimir() # es trampa -> ['Perro', 'Pato', 'Ganzo', 'Rana', 'Mono']
        print()

        print("\nPopeo algunos valores: ")
        print(animales.pop()) # Mono
        print(animales.pop()) # Rana
        print(animales.pop()) # Ganzo
        print(animales.pop()) # Pato
        print(animales.pop()) # Perro

        print("\nLa pila ha quedado vacía: ")
        animales.imprimir() # es trampa --> [None, None, None, None, None]

        print("\nIntento popear de una pila vacía")
        try:
            print(animales.pop()) # desencolar de una pila vacía tira error

        except Exception as e:
            print(f"\nHay un error: {e}") # -> La pila está vacía

main()
print()