
class Cola():
    def __init__(self,tam):
        self.head=0
        self.tail=0
        self.tam=tam
        self.arr=[None]*tam

    def enqueue(self,e):
        if(self.tail-self.head==self.tam):
            print("ENQUEUE ERROR: cola llena")
        else:
            self.tail=self.tail%self.tam
            self.arr[self.tail]=e
            self.tail=self.tail+1
        
    def dequeue(self):
        if(self.tail-self.head==0):
            print("DEQUEUE ERROR: cola vacia")
            return None
        else:
            self.head=self.head%self.tam
            res=self.arr[self.head]
            self.head+=1
            return res
        

def leerArch(ruta):
    f=open(ruta,'r')
    while True:
        line=f.readline()
        if not line:
            break
        strline=line.strip().split(',')

    return strline
        
def operar(cola: Cola,operaciones):
    i=0
    while i<len(operaciones):
        if operaciones[i]=='+':
            i+=1
            cola.enqueue(int(operaciones[i]))
        else:
            print(f'DEQUEUE: {cola.dequeue()}')
        i+=1

        

            

def main():
    cola=Cola(5)

    operaciones=leerArch('/home/ignacio-berkelaar/Documents/GitHub/practicos/02.EstructurasLineales/datos1.csv')
    operar(cola,operaciones)
    
     #LOS ERROR SON PARA VER SI DETECTA SI ESTA VACIA O LLENA

    
    


if __name__=='__main__':
    main()