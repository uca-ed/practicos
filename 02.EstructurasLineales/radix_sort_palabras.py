import sys

def radix_sort_palabras(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        palabras = [palabra.strip().lower() for palabra in archivo if palabra.strip()]
    if not palabras:
        return []
    max_len = max(len(palabra) for palabra in palabras)
    sentinela = "\0"
    normalizadas = [palabra.ljust(max_len, sentinela) for palabra in palabras]
    for posicion in range(max_len - 1, -1, -1):
        conteo = [[] for _ in range(256)]
        for palabra in normalizadas:
            indice = ord(palabra[posicion])
            conteo[indice].append(palabra)
        normalizadas = [palabra for grupo in conteo for palabra in grupo]
    resultado = [palabra.replace(sentinela, "") for palabra in normalizadas]
    return resultado

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python radix_sort_palabras.py archivo_palabras")
        sys.exit(1)
    resultado = radix_sort_palabras(sys.argv[1])
    for palabra in resultado:
        print(palabra)
