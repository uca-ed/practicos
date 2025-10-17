# EJERCICIO 2

class stack():
    def __init__(self):
        self.stack = [None]*5
        self.len_q = 5
        self.top = 0
    
    def push(self,value):
        if self.top >= self.len_q:
            print("el stack esta lleno. {} no entra al stack.".format(value))
            return "el stack esta lleno"
        else:
            self.stack[self.top] = value
            self.top += 1

    def pop(self):
        if self.top == 0:
            print("el stack esta vacio")
            return "el stack esta vacio"
        else:
            self.stack[self.top - 1] = None
            self.top -= 1


def main():
    mi_lista = stack()
    mi_lista.push(5)
    mi_lista.push(25)
    mi_lista.push(3)
    mi_lista.push(2)
    mi_lista.push(1)
    mi_lista.pop()
    mi_lista.push(1)
    print("el stack es:",mi_lista.stack)
    mi_lista.push(2) # se pasa de rango
    mi_lista.pop()
    mi_lista.pop()
    print("el stack esta:",mi_lista.stack)


main()