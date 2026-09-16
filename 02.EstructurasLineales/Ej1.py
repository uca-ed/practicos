
def inicializarCola():
    cola={"arr": [None]*5, "front": 0, "bot": 0, "cant": 0}
    return cola #arreglo de tamanio fijo

def encolar(cola, valor):
    if len(cola["arr"])==cola["cant"]:
        return "[ERROR] Overflow"
    if valor==None:
        return "[ERROR] No hay valor a encolar"
    cola["arr"][cola["bot"]]=valor
    cola["cant"]+=1
    cola["bot"]=(cola["bot"]+1)%len(cola["arr"])

def desencolar(cola):
    if cola["cant"]==0:
        return "[ERROR] Underflow"
    valor=cola["arr"][cola["front"]]
    cola["arr"][cola["front"]]=None
    cola["cant"]-=1
    cola["front"]=(cola["front"]+1)%len(cola["arr"])
    return valor

def procesar_archivo(ruta_archivo, cola):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            comando = partes[0].strip()

            if comando == "ENQUEUE":
                valor = int(partes[1].strip())
                res = encolar(cola, valor)
                if res:
                    print(res)

            elif comando == "DEQUEUE":
                res = desencolar(cola)
                if res == "[ERROR] Underflow":
                    print(res)
                else:
                    print(f"Desencolado: {res}")



c = inicializarCola()
procesar_archivo("operaciones.txt", c)

print("\nEstado final:")
print("Arreglo:", c["arr"])
print("Cantidad:", c["cant"])