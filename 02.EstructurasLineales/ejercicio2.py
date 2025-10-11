"""
2. Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones
sobre pilas y operar, partiendo de una pila vacía. Se debe mostrar el resultado final.
"""

def cargar_pila(nombre_archivo):
    pila = [] 
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                operacion = partes[0].upper()
                if operacion == "PUSH":
                    valor = partes[1]
                    pila.append(valor)  
                elif operacion == "POP":
                    if pila:
                        pila.pop()  
        return pila
    except FileNotFoundError:
        return None

def calculo_postfijo_pila(pila):
    aux = []  
    while pila:
        x = pila.pop(0)  
        if x.isdigit():
            aux.append(int(x))
        else:
            b = aux.pop()
            a = aux.pop()
            if x == '+':
                aux.append(a + b)
            elif x == '-':
                aux.append(a - b)
            elif x == '*':
                aux.append(a * b)
            elif x == '/':
                aux.append(a / b)
    return aux[0]

if __name__ == "__main__":
    archivo = "ejemplo2.txt"
    P = cargar_pila(archivo)
    print("Pila final:", P)
    res = calculo_postfijo_pila(P)
    print("Resultado del calculo postfijo:", res)
