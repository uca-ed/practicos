#Ej_02
#Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar,
#partiendo de una pila vacía. Se debe mostrar el resultado final.
##Quiero agradecer a Chio Code, porque me estas explicando todo
# + ese pdf de listas enlazadas, posta muy util lol
#Tambien quiero agradecer a geekCode pero estoy muy segura que agarraron el pdf como base

class ListNode :
    #Creo nodos, se refieren a si mismo para info
    def __init__ (self, data) :
        self.data = data
        self.next = None #A lo ultimo siempre va a estar vacío
        
def traversal(head):
    curNode = head #Head va a ser el primer nodo de la lista
    while curNode is not None: #Si es None es que no hay más para agarrar
        print (curNode.data)
        curNode = curNode.next #Es el siguienet

def search(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None #puede que no este lo que buscamos
    

def insert(head, data):
    #Siento que este se explica solo lol
    newNode = ListNode(data)
    newNode.next = head
    
    return newNode

def delete(head):
    #Me fijo que no este vacía
    if head is None:
        return None
    
    tempNode = head #Guardo la variable temporal
    head = head.next #Cambio cual es el primero en la fila

    del tempNode #Elimino el primero
    
    return head

def main():
    #Siempre me olvido que existe la funcion main lol
    head = ListNode(11)
    head.next = ListNode(67)
    head.next.next = ListNode(21)
    head.next.next.next = ListNode(98)
    
    #print(search(head, 19)) #Osea, te da un True si está y un false si no existe
    
    print ("Voy a insertar el numero 15 en mi PILA")
    print ("Antes:")
    traversal(head)
    head = insert(head, 15)
    print ("después:")
    traversal(head)
    print("Ahora voy a eliminarlo, porque esto es una pila:")
    head = delete(head)
    print ("Y mi PILA vuelve a ser:")
    traversal(head)

main()



#Despues puedo hacer la pila