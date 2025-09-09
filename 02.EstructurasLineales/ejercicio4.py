"""4. Implementar Radix Sort y ordenar las palabras de los archivos indicados.
ORDEN: POR PUNTOS QUE SUMA LA FICHA --> NUMERO (MENOR A MAYOR) --> COLOR (ALFABÉTICAMENTE)"""

#Clase para crear objeto cola:
class ColaSobreArreglo:
    def __init__(self,tam):
        self.tam=tam
        self.data=[None]*tam
        self.front=0
        self.rear=-1
    
    def estaVacia(self):
        return self.data[self.front] == None 
    
    def estaFull(self):
        return (self.data[self.front] != None and (self.rear + 1)%self.tam == self.front)
    
    def enqueue(self,ele):
        if(self.estaFull()):
            print("Error, arreglo full")
        else:
            self.data[(self.rear + 1)%self.tam] = ele
            self.rear = (self.rear + 1)%self.tam

    def dequeue(self):
        if(self.estaVacia()):
            print("Error, arreglo vacío")
        else:
            rta = self.data[self.front]
            self.data[self.front]=None
            self.front = (self.front + 1)%self.tam
            return rta
        
    def imprimir(self):
        if(self.estaVacia()==False):
            ini=self.front
            for i in range(self.tam):
                ele=self.data[ini]
                if ele != None:
                    print(ele)
                    ini = (ini+1)%self.tam
                    if self.data[ini]==None:
                        break


#Primero creo una cola Q compuesta de listas de los elementos levantados por el archivo
colaOriginal = ColaSobreArreglo(107)
def cargarColaDesdeCSV(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            partes = linea.split(",")
            colaOriginal.enqueue(partes)
        colaOriginal.dequeue()


cargarColaDesdeCSV("02.EstructurasLineales/burako_fichas_mezcladas.csv")

#Primero creo las referencias:

ref_puntaje = {"50":0, "20":1, "15":2, "10":3, "5":4}
ref_numero = {"1": 0,"2": 1,"3": 2,"4": 3,"5": 4,"6": 5,"7": 6,"8": 7,"9": 8,"10": 9,"11": 10,"12": 11,"13": 12,"carita": 13}
ref_color   = {"amarillo":0, "azul":1, "negro":2, "rojo":3}

referencias_ordenadas = [
    (2, ref_color),   # campo 2 = color
    (1, ref_numero),  # campo 1 = número
    (0, ref_puntaje)  # campo 0 = puntaje
]
#Ahora implemento Radix Sort
def radixSort(Q,refe):
    p = len(refe)
    for i in range(p):
        d_actual = refe[i][1]
        campo_actual = refe[i][0]
        colas_para_i=len(d_actual)
        lista_de_colas = []

        for j in range(colas_para_i):
            cola = ColaSobreArreglo(107)
            lista_de_colas.append(cola)
        
        while not Q.estaVacia():
            ele = Q.dequeue()
            k = d_actual[ele[campo_actual]]  # acceso O(1)
            lista_de_colas[k].enqueue(ele)
        for c in lista_de_colas:
             while not c.estaVacia():
                Q.enqueue(c.dequeue())

    return Q
        

colaOrdenada = radixSort(colaOriginal,referencias_ordenadas)
colaOrdenada.imprimir()
        
    