# cola_circular.py
import sys

CAPACIDAD = 60

class Cola:
    def __init__(self):
        self.datos = [None] * CAPACIDAD
        self.inicio = 0
        self.cantidad = 0

    def encolar(self, valor: int) -> bool:
        if self.cantidad < CAPACIDAD:
            idx = (self.inicio + self.cantidad) % CAPACIDAD
            self.datos[idx] = valor
            self.cantidad += 1
            print(f"[Debug] Encolar {valor} | inicio={self.inicio} cantidad={self.cantidad}")
            return True
        print("[Error] Cola llena")
        return False

    def desencolar(self):
        if self.cantidad > 0:
            rta = self.datos[self.inicio]
            print(f"[Debug] Desencolar idx={self.inicio} -> {rta}", end="")
            self.cantidad -= 1
            self.inicio = (self.inicio + 1) % CAPACIDAD
            print(f" | nuevo_inicio={self.inicio}")
            return rta
        print("[Error] Cola vacia")
        return None

def leer_enteros():
    with open("valores.txt", "r", encoding="utf-8") as f:
        for token in f.read().split():
            try:
                yield int(token)
            except ValueError:
                pass  # ignorar tokens no numéricos

def main():
    fuente=leer_enteros()

    q = Cola()


    for x in fuente:
        if not q.encolar(x):
            break


    primero = q.desencolar()
    segundo = q.desencolar()
    print(f"Primer elemento de la cola: {primero}\nSegundo: {segundo}")


    for x in fuente:
        if not q.encolar(x):
            break


    print("\n----- Estado de la cola -----")
    print(f"inicio={q.inicio} | cantidad={q.cantidad} | capacidad={CAPACIDAD}")
    for i in range(q.cantidad):
        idx = (q.inicio + i) % CAPACIDAD
        print(f"datos[{idx}]={q.datos[idx]}")

if __name__ == "__main__":
    main()
