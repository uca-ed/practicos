class Celda:
    def __init__(self, indice):
        self.valor = None
        self.siguiente = None
        self.indice = indice

    def verValor(self):
        return self.valor

    def push(self,valor):
        if self.valor == None:
            self.valor = valor
            self.siguiente = Celda(self.indice + 1) # creo que asi
        else:
            self.siguiente.push(valor)

    def pop(self):
        if self.valor == None:
            raise Exception("Pop a una lista vacía")
        if self.siguiente == None:
            valor = self.valor 
            self.valor = None
            return valor
        elif self.siguiente != None:
            if self.siguiente.verValor() == None:
                self.siguiente = None
                valor = self.valor 
                self.valor = None
                return valor
            else:
                return self.siguiente.pop()
            
    
    def cambiarEn(self, indice, valor):
        if indice < 0:
            raise Exception("Indice fuera de rango")
        elif indice == self.indice:
            if self.valor == None:
                raise Exception("Indice fuera de rango")
            else:
                self.valor = valor
        elif indice > self.indice:
            self.siguiente.cambiarEn(indice, valor)

    def verEn(self, indice):
        if indice < 0:
            raise Exception("Indice fuera de rango")
        elif indice == self.indice:
            if self.valor == None:
                raise Exception("Indice fuera de rango")
            else:
                return self.valor
        elif indice > self.indice:
            return self.siguiente.verEn(indice)


def main():
    animales = Celda(0)
    animales.push("zebra")
    animales.push("orangutan")
    animales.push("macaco")

    print("Hago 3 push y los veo segun el indice que quiera en la lista:\n")
    enRango = True
    i = 0
    while enRango:
        try:
            print(f"Indice {i} : {animales.verEn(i)}")
            i += 1
        except Exception as e:
            print("Esos son todos.")
            enRango = False


    print(f"\nCambio el valor en el Indice {1} por {"camello"}:\n")
    animales.cambiarEn(1,"camello")
    enRango = True
    i = 0
    while enRango:
        try:
            print(f"Indice {i} : {animales.verEn(i)}")
            i += 1
        except Exception as e:
            print("Esos son todos.")
            enRango = False

    print("\nHago los pops:\n")
    print("Pop() : "+animales.pop())
    print("Pop() : "+animales.pop())
    print("Pop() : "+animales.pop())

    print("\nIntento hacer Pop() en una lista vacía:\n")
    try:
        animales.pop()
    except Exception as e:
        print(f"Error: {e}")


print("\nEjecicio 3 : Lista enlazada simple\n")
main()
print()