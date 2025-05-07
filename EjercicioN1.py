import Main

### EJERCICIO 1 ###

### Aclaracion: NO Consideramos minimal si se apunta a sí mismo ###
### Aclaracion: NO Consideramos maximal si se apunta a sí mismo ###
### Aclaracion: SI consideramos que la vecindad derecha de un nodo incluye el mismo nodo ###
### Aclaracion: SI consideramos que la vecindad izquierda de un nodo incluye el mismo nodo ###

def minimal_json(estructura):
    nodos = estructura['E'].keys()
    minimos = []
    for nodo in nodos:
        if vecindad_izquierda_json(estructura, nodo) == []:
            minimos.append(nodo)
    return minimos

def minimal_csv(matriz):
    minimos = []
    for nodo in range(len(matriz)):
        if vecindad_izquierda_csv(matriz, nodo) == []:
            minimos.append(nodo + 1)
    return minimos

def maximal_json(estructura):
    nodos = estructura['E'].keys()
    maximos = []
    for nodo in nodos:
        if vecindad_derecha_json(estructura, nodo) == []:
            maximos.append(nodo)
    return maximos

def maximal_csv(matriz):
    maximos = []
    for nodo in range(len(matriz)):
        if vecindad_derecha_csv(matriz, nodo) == []:
            maximos.append(nodo + 1)
    return maximos

def vecindad_derecha_json(estructura, nodo_objetivo):
    return estructura['E'][nodo_objetivo]

def vecindad_derecha_csv(matriz, nodo_objetivo):
    vecinos = []
    for j in range(len(matriz[nodo_objetivo])):
        if matriz[nodo_objetivo][j] == 1:
            vecinos.append(j + 1)
    return vecinos

def vecindad_izquierda_json(estructura, nodo_objetivo):
    vec_izquierda = []
    for nodo in estructura['E']:
        if nodo_objetivo in estructura['E'][nodo]:
            vec_izquierda.append(nodo)
    return vec_izquierda

def vecindad_izquierda_csv(matriz, nodo_objetivo):
    vec_izquierda = []
    for i in range(len(matriz)):
        if matriz[i][nodo_objetivo] == 1:
            vec_izquierda.append(i + 1)
    return vec_izquierda

def ejercicio_1_JSON(estructura):
    print("1A: Nodos mínimos:", minimal_json(estructura))
    print("1B: Nodos máximos:", maximal_json(estructura))
    
    nodo = input("Ingrese el nodo para analizar vecindades (ej. '100'): ")
    print(f"1C: Vecindad derecha en {nodo}:", vecindad_derecha_json(estructura, nodo))
    print(f"1D: Vecindad izquierda en {nodo}:", vecindad_izquierda_json(estructura, nodo))

def ejercicio_1_CSV(matriz):
    print("1A: Nodos mínimos:", minimal_csv(matriz))
    print("1B: Nodos máximos:", maximal_csv(matriz))
    
    while True:
        try:
            nodo = int(input(f"Ingrese el nodo (entre 1 y {len(matriz)}) para analizar vecindades: "))
            if 1 <= nodo <= len(matriz):
                break
            else:
                print("Nodo fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    print(f"1C: Vecindad derecha en {nodo}:", vecindad_derecha_csv(matriz, nodo - 1))
    print(f"1D: Vecindad izquierda en {nodo}:", vecindad_izquierda_csv(matriz, nodo - 1))


# Se debe ingresar el nombre del archivo. 
# Este se debe encontrar en la carpeta archivos_ej1
# ej: 'hola.json'
def main_1(arch):

    tipo = Main.identificar_archivo(arch)
    print("Archivo: ", arch)

    if tipo == 'json':
        estructura = Main.cargar_json('archivos_ej1/' + arch)
        ejercicio_1_JSON(estructura)
        print()
    
    elif tipo == 'csv':
        matriz_1 = Main.leer_matriz_csv('archivos_ej1/' + arch)
        ejercicio_1_CSV(matriz_1)
        print()

main_1('01.json')