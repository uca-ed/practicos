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
        datos = []
        lector_csv = csv.reader(archivo_csv)
        for palabra in list(lector_csv): # una lista de python con 
            datos.append(palabra[0])
        print(f"Utilizo los valores de la siguiente lista:")
        for dato in datos:
            print(dato)

        animales = PilaTamañoFijo(5)

        print("\nEjercicio 2 : Pila sobre arreglo\n")
        
        print("\Apilo valores (0: apilado | -1: pila llena): ")        
        for dato in datos:
            print(f"\nP <-- Resultado: {animales.push(datos.pop(0))}")
            animales.imprimir() # haciendo trampa
        print(f"\nP <-- Resultado: {animales.push(datos.pop(0))}")

        print("\nValores dentro de la pila: ")
        animales.imprimir() # haciendo trampa -> ['Perro', 'Pato', 'Ganzo', 'Lobo', 'Rana']
        print()

        print("\Desapilo hasta que quede vacía: ")
        try:
            while(1): 
                print(f"\nP --> {animales.pop()}")
                animales.imprimir() # haciendo trampa

        except Exception as e:
            print("\nIntento seguir desapilando:")
            print(f"\nHay un error: {e}") # -> La pila está vacía
            
            
            

main()
print()