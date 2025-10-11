"""
1. Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones
sobre colas y operar, partiendo de una cola vacía. Se debe mostrar el resultado final. 
"""

def cargar_cola_postfijo(nombre_archivo):
    cola = [] 
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                operacion = partes[0].upper()
                if operacion == "ENQUEUE":
                    valor = partes[1]
                    cola.append(valor)  
                elif operacion == "DEQUEUE":
                    if cola:
                        cola.pop(0) 
        return cola
    except FileNotFoundError:
        return None

def calculo_postfijo(cola):
    pila = []
    while cola:
        x = cola.pop(0)
        if x.isdigit():
            pila.append(int(x))
        else:
            b = pila.pop()
            a = pila.pop()
            if x == '+':
                pila.append(a + b)
            elif x == '-':
                pila.append(a - b)
            elif x == '*':
                pila.append(a * b)
            elif x == '/':
                pila.append(a / b)

    return pila[0]

if __name__ == "__main__":
    archivo = "ejemplo1.txt"
    Q = cargar_cola_postfijo(archivo)
    print("Cola final:", Q)
    res = calculo_postfijo(Q)
    print("Resultado del calculo postfijo:", res)
