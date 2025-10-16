def ordenarBucket(buckets):
    listaOrdenada=[]
    for clave in sorted(buckets.keys()):
        listaOrdenada.append(clave)
    buckets.clear()

    for clave in listaOrdenada:
        buckets[clave]=[]

    return buckets



def radix_sort(palabras):
    max_len = max(len(p) for p in palabras)
    palabras = [p.ljust(max_len) for p in palabras]

    for i in range(max_len - 1, -1, -1):
        print(f"orden {i}")

        buckets = {}
        buckets.clear()
        for palabra in palabras:
            clave = palabra[i]
            if(not clave in buckets.keys()):
                buckets[clave]=[]
                print(clave)

        buckets=ordenarBucket(buckets)
        print(f"BUCKET ORDENADO:{buckets.keys()}")
        
        for clave in buckets:
            for palabra in palabras:
                if(palabra[i]==clave):
                    buckets[clave].append(palabra)
       
        nueva_lista = []
        for clave in buckets:
            nueva_lista.extend(buckets[clave])
        palabras = nueva_lista


        for clave in buckets:
            print(f"-{clave}: {buckets[clave]}")
    
    return [p.strip() for p in palabras]

def leerPalabras(nombreArchivo):
    palabras=[]
    with open(nombreArchivo, "r") as f:
        for linea in f:
            linea=linea.strip()
            palabras.append(linea)
    f.close()
    return palabras

def main():
    palabras=leerPalabras("palabrasOrdenar.txt")
    print("PALABRAS SIN ORDENAR: ")
    print(palabras)

    ordenadas = radix_sort(palabras)


    print("PALABRAS ORDENADAS:")
    for p in ordenadas:
        print(p)

main()