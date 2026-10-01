class ColaArreglo:
    def __init__(self, capacidad=100):
        self.max = capacidad
        self.datos = [None] * self.max
        self.frente = 0
        self.fin = -1
        self.tamano = 0

    def enqueue(self, valor):
        if self.tamano == self.max:
            print("Error: Cola Llena (Overflow)")
            return
        self.fin = (self.fin + 1) % self.max
        self.datos[self.fin] = valor
        self.tamano += 1

    def dequeue(self):
        if self.tamano == 0:
            print("Error: Cola Vacía (Underflow)")
            return None
        valor = self.datos[self.frente]
        self.frente = (self.frente + 1) % self.max
        self.tamano -= 1
        return valor

    def mostrar_estado(self):
        elementos = []
        idx = self.frente
        for _ in range(self.tamano):
            elementos.append(self.datos[idx])
            idx = (idx + 1) % self.max
        print(f"Estado final de la Cola (frente a fin): {elementos}")


def procesar_archivo_cola(ruta_archivo):
    cola = ColaArreglo()
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(',')
                comando = partes[0].strip().upper()

                if comando == "ENQUEUE":
                    valor = int(partes[1].strip())
                    cola.enqueue(valor)
                elif comando == "DEQUEUE":
                    cola.dequeue()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")

    cola.mostrar_estado()


if __name__ == "__main__":
    procesar_archivo_cola("operaciones_cola.txt")
