

class Nodo:
    def __init__(self, dato):
            self.data = dato
            self.next = None


class ListNode:
     
    def imprimir(cabecera):
        curNodo = cabecera
        while curNodo is not None:
            print (curNodo.data)
            curNodo = curNodo.next

    def buscar(cabecera, valor):
        curNodo = cabecera
        while curNodo is not None and curNodo.data!=valor:
            curNodo = curNodo.next
        return curNodo 

    def insertarAlComienzo(cabecera, valor):
        nuevoNodo = Nodo(valor)
        nuevoNodo.next = cabecera 
        cabecera = nuevoNodo

        return cabecera

    def insertarOrdenado(cabecera, valor):
        nuevoNodo = Nodo(valor)

        if cabecera is None or valor < cabecera.data:
            return ListNode.insertarAlComienzo(cabecera,valor)

        curNodo = cabecera
        while curNodo.next is not None and curNodo.next.data < valor:
            curNodo = curNodo.next

        nuevoNodo.next = curNodo.next
        curNodo.next = nuevoNodo

        return cabecera

    def eliminar(cabecera, valor):

        prevNodo = None
        curNodo = cabecera

        while curNodo is not None and curNodo.data != valor:
            prevNodo = curNodo
            curNodo = curNodo.next

        if curNodo is not None:
            if curNodo is cabecera:
                cabecera = curNodo.next
            else:
                prevNodo.next = curNodo.next
        else:
            print(f'No existe {valor} en la lista. No se puede eliminar')
        return cabecera

def main():
    cabecera = None

    archivo = open("listas_operations.txt")
    for linea in archivo:
        datos = linea.strip().split(",")
        operacion = datos[0]
        valor = int(datos[1])

        if operacion == "INSERTAR":
            cabecera = ListNode.insertarOrdenado(cabecera,valor)
        elif operacion == "ELIMINAR":
            cabecera = ListNode.eliminar(cabecera,valor)
        elif operacion =='BUSCAR':
            nodito = ListNode.buscar(cabecera,valor)
            if nodito is not None:
                print(f"Se encontro el {valor}")
            else:
                print(f'No se encontro a {valor}')
    archivo.close()

    ListNode.imprimir(cabecera)



main()
        



