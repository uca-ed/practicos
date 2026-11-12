def iniciarPila():
    pila={"arr": [None]*5,"tope":0}
    return pila
def push(pila, valor):
    if len(pila["arr"])==pila["tope"]:
        return "[ERROR] Overflow"
    pila["arr"][pila["tope"]]=valor
    pila["tope"]+=1
def pop(pila):
    if(pila["tope"]-1)<0:
        return "[ERROR] Underflow"
    valor=pila["arr"][pila["tope"]-1]
    pila["arr"][pila["tope"]-1]=None
    pila["tope"]-=1
    return valor

def procesar_archivo(ruta_archivo, cola):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            partes = linea.split(",")
            comando = partes[0].strip()

            if comando == "PUSH":
                valor = int(partes[1].strip())
                res = push(cola, valor)
                if res:
                    print(res)

            elif comando == "POP":
                res = pop(cola)
                if res == "[ERROR] Underflow":
                    print(res)
                else:
                    print(f"Removido: {res}")



c = iniciarPila()
procesar_archivo("operaciones2.txt", c)

print("\nEstado final:")
print("Arreglo:", c["arr"])
print("Tope:", c["tope"])
