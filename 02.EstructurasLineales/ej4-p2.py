#Implementar Radix Sort y ordenar las palabras de los archivos indicados.

def radix_sort(arr):
    if not arr:
        return arr
    
    max_len=max(len(p) for p in arr)
    R=256
    for j in range(max_len-1,-1,-1):
        colas=[[] for _ in range(R)]
        for palabra in arr:
            if j<len(palabra):
                indice=ord(palabra[j])
            else:
                indice=0
            colas[indice].append(palabra)
        lista=[]
        for cola in colas:
            lista.extend(cola)
    return lista

def main():
    with open(r"C:\Users\danie\OneDrive\Documentos\estructura de datos\practica2\ej4.txt") as f:
        for linea in f:
            palabras=linea.split(", ")
            print(palabras)
    print(radix_sort(palabras))

main()