#Ejercicio 4: Implementar Radix Sort y ordenar las palabras de los archivos indicados.



def orden(alfabeto):
    return {letra: i for i, letra in enumerate(alfabeto)}

def radix_sort_personalizado(palabras, alfabetos_por_posicion):
    for pos in reversed(range(len(alfabetos_por_posicion))):
        alf = alfabetos_por_posicion[pos]
        orden_alf = orden(alf)
        # Ordenar por contenedor
        contenedores = [[] for _ in range(len(alf))]
        for palabra in palabras:
            indice = orden_alf[palabra[pos]]
            contenedores[indice].append(palabra)
        # Reconstruir lista
        palabras = [p for contenedor in contenedores for p in contenedor]
    return palabras

def leer_palabras_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def main():
    sigma_1 = ['A', 'B', 'C']           # Para la letra inicial
    sigma_2 = ['1', '3', '2', '4']      # Para los números

    alfabetos_por_posicion = [sigma_1, sigma_2, sigma_2] 
    palabras = leer_palabras_desde_archivo("palabras.txt")

    print("Originales:", palabras)
    ordenadas = radix_sort_personalizado(palabras, alfabetos_por_posicion)
    print("Ordenadas:", ordenadas)

if __name__ == "__main__":
    main()
