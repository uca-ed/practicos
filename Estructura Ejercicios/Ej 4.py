orden_palos = {'Espadas': 0, 'Copas': 1, 'Bastos': 2, 'Oros': 3}

def leer_cartas(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    cartas = []
    for linea in lineas:
        palo, numero = linea.strip().split()
        cartas.append((palo, int(numero)))
    return cartas

def radix_sort_cartas(cartas):
    # Por número (menos significativo)
    queues_num = {}
    for carta in cartas:
        num = carta[1]
        queues_num.setdefault(num, []).append(carta)

    print("Distribución por número:")
    for k in sorted(queues_num):
        print(f"{k}: {queues_num[k]}")

    cartas_ordenadas_por_num = []
    for k in sorted(queues_num):
        cartas_ordenadas_por_num.extend(queues_num[k])

    # Por palo (más significativo)
    queues_palo = {}
    for carta in cartas_ordenadas_por_num:
        orden = orden_palos[carta[0]]
        queues_palo.setdefault(orden, []).append(carta)

    print("\nDistribución por palo:")
    for k in sorted(queues_palo):
        palo = [nombre for nombre, val in orden_palos.items() if val == k][0]
        print(f"{palo}: {queues_palo[k]}")

    resultado = []
    for k in sorted(queues_palo):
        resultado.extend(queues_palo[k])
    return resultado

if __name__ == "__main__":
    archivo = "Archivo para ej/cartas.txt"
    cartas = leer_cartas(archivo)
    resultado = radix_sort_cartas(cartas)

    print("\nResultado:")
    for carta in resultado:
        print(carta)
