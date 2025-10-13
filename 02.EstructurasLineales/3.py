class Nodo():
    def __init__(self,e):
        self.val=e
        self.sig=None
    
    def agregar(self,e):
        if self.sig!=None:
            self.sig.agregar(e)
        else:
            self.sig=Nodo(e)
    
    def mostrar(self):
        print(f'{self.val}',end='')
        if self.sig!=None:
            print(', ',end='')
            self.sig.mostrar()



class Lista():
    def __init__(self):
        self.nodo=None

    def agregar(self,e):
        if self.nodo==None:
            self.nodo=Nodo(e)
        else:
            self.nodo.agregar(e)

    def mostrar(self):
        if self.nodo!=None:
            print('LISTA: [',end='')
            self.nodo.mostrar()
            print(']')
        else:
            print('LISTA VACIA')





def main():
    ls=Lista()

    ls.mostrar()

    ls.agregar(1)
    ls.agregar(2)
    ls.agregar(4)
    ls.agregar(99)
    ls.agregar(173)

    ls.mostrar()

if __name__=='__main__':
    main()