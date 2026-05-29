#main.py

import estructuras_lineales as el
import sorting_topologico as st
import mapeo_universidad as mu

def generar_archivos_prueba():
    with open("operaciones_cola.txt", "w") as f:
        f.write("ENQUEUE,1\nENQUEUE,2\nENQUEUE,3\nENQUEUE,4\nDEQUEUE,\nDEQUEUE,\n")
        
    with open("operaciones_pila.txt", "w") as f:
        f.write("PUSH,1\nPUSH,2\nPUSH,3\nPOP,\nPOP,\n")

def main():
    generar_archivos_prueba()

    el.procesar_operaciones_cola("operaciones_cola.txt")

    el.procesar_operaciones_pila("operaciones_pila.txt")

    cabeza = None
    for valor in ["Estructuras", "De", "Datos", "UCA"]:
        cabeza = el.insertar_lista(cabeza, valor)
    print(f"Resultado de la lista: {el.mostrar_lista(cabeza)}\n")

    palabras = ["datos", "algoritmo", "cola", "pila", "uca", "carola", "fiorella"]
    ordenadas = st.radix_sort_palabras(palabras)
    print(f"Ordenado por Radix Sort: {ordenadas}\n")

    nodos = ["A", "B", "C", "D", "E"]
    grafo_valido = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
    resultado_tsort = st.calcular_t_sort(nodos, grafo_valido)
    print(f"Resultado T-Sort Estructura Válida: {resultado_tsort}")
    
    grafo_ciclico = {"A": ["B"], "B": ["C"], "C": ["A"]}
    resultado_ciclico = st.calcular_t_sort(["A", "B", "C"], grafo_ciclico)
    print(f"Resultado T-Sort Estructura Cíclica: {resultado_ciclico}\n")

    uni = mu.GestionUniversidad1D()
    
    idx, porc = uni.mayor_porcentaje_ocupacion()
    print(f"a. Índice lineal con mayor ocupación: {idx} ({porc*100:.2f}%)")
    
    promedios = uni.promedio_alumnos_por_piso(BH=10)
    print(f"b. Promedio de alumnos por piso en bloque horario 10: {promedios}")
    
    alas = uni.total_alumnos_por_ala(E=0, P=2, BH=10)
    print(f"c. Total de alumnos presentes en bloque horario 10 (Edificio 0, Piso 2): {alas}")

if __name__ == "__main__":
    main()