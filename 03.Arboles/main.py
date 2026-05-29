#main.py

import os
import arbol_arreglo as aa
import arbol_avl as avl

def generar_archivo_inserciones():
    with open("datos_avl.txt", "w") as f:
        f.write("10\n20\n30\n40\n50\n25\n")

def cargar_datos_avl(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        return []
    valores = []
    with open(ruta_archivo, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                valores.append(int(linea))
    return valores

def main():
    generar_archivo_inserciones()

    datos_arbol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    grado_arbol = 3
    
    arbol_arr = aa.ArbolRepresentadoEnArreglo(datos_arbol, grado_arbol)
    
    altura = arbol_arr.obtener_altura_sin_recorrido()
    print(f"a) Altura del arbol (calculada sin recorrer): {altura}")
    
    recorrido_pre = arbol_arr.barrido_pre_orden()
    print(f"b) Barrido en pre-orden: {recorrido_pre}\n")

    valores_a_insertar = cargar_datos_avl("datos_avl.txt")
    arbol_balanceado = avl.ArbolAVL()
    
    for valor in valores_a_insertar:
        arbol_balanceado.insertar(valor)
        
    print(f"Arbol AVL creado. Estructura ordenada (In-Order): {arbol_balanceado.obtener_in_order()}")

if __name__ == "__main__":
    main()