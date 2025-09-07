# ============================================================
# Implementación de una Cola (Queue) utilizando un arreglo fijo
# con comportamiento circular.
#
# Características:
# - Capacidad máxima fija definida en el constructor.
# - Operaciones soportadas:
#     * enqueue(x): encolar elemento al final.
#     * dequeue(): desencolar elemento desde el frente.
# - Almacena enteros, pero se puede adaptar a cualquier tipo.
# - Lectura de operaciones desde archivo de texto.
# ============================================================

class Cola:
    def __init__(self, capacidad=100):
        """
        Constructor de la cola.
        :param capacidad: tamaño máximo del arreglo subyacente.
        """
        self.arr = [None] * capacidad   # arreglo circular
        self.cap = capacidad            # capacidad máxima
        self.ini = 0                    # índice del primer elemento (frente de la cola)
        self.tam = 0                    # cantidad de elementos almacenados

    def enqueue(self, x):
        """
        Inserta un elemento al final de la cola.
        :param x: elemento a insertar.
        """
        if self.tam == self.cap:
            raise OverflowError("Cola llena")
        # calcular posición física en el arreglo circular
        idx = (self.ini + self.tam) % self.cap
        self.arr[idx] = x
        self.tam += 1

    def dequeue(self):
        """
        Elimina y devuelve el primer elemento de la cola.
        :return: valor del elemento eliminado.
        """
        if self.tam == 0:
            raise IndexError("Cola vacía")
        # elemento a devolver
        x = self.arr[self.ini]
        # avanzar el puntero de inicio circularmente
        self.ini = (self.ini + 1) % self.cap
        self.tam -= 1
        return x

    def __str__(self):
        """
        Representación en string de la cola.
        Muestra los elementos en orden lógico (frente -> fondo).
        """
        return "[" + ", ".join(str(self.arr[(self.ini+i) % self.cap]) for i in range(self.tam)) + "]"


# ============================================================
# Función de utilidad para ejecutar operaciones desde archivo.
# El archivo debe contener una instrucción por línea:
#   ENQUEUE valor   -> encola 'valor'
#   DEQUEUE         -> desencola un elemento
# Ejemplo de archivo:
#   ENQUEUE 10
#   ENQUEUE 20
#   DEQUEUE
# ============================================================
def ejecutar_operaciones_cola(nombre_archivo):
    cola = Cola()  # comenzamos con cola vacía
    with open(nombre_archivo) as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue  # ignorar líneas vacías
            if partes[0].upper() == "ENQUEUE":
                cola.enqueue(int(partes[1]))
            elif partes[0].upper() == "DEQUEUE":
                cola.dequeue()
    print("Cola final:", cola)

ejecutar_operaciones_cola(r"C:\Users\Fede\Documents\GitHub\practicos\02.EstructurasLineales\cola1.txt")


# ============================================================
# EJEMPLO DE USO
# Crear un archivo llamado 'cola.txt' con el siguiente contenido:
# ENQUEUE 10
# ENQUEUE 20
# ENQUEUE 30
# DEQUEUE
# ENQUEUE 40
#
# Y luego ejecutar:
# ejecutar_operaciones_cola("cola.txt")
#
# Salida esperada:
# Cola final: [20, 30, 40]
# ============================================================
