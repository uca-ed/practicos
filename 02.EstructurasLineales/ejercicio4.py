#4) Radix Sort
def radix_sort(palabras):
    if not palabras:
        return []

    max_len = max(len(p) for p in palabras)

    for pos in range(max_len - 1, -1, -1): #recorre desde la der hasta la izq
        num_letras=27
        letras=[]
        for i in range(num_letras):
            letras.append([]) #va a ser una lista de 27 listas vacias
        for palabra in palabras:
            char='\0'
            if pos < len(palabra):
                char=palabra[pos].lower() #para minusculas
            if char == '\0':
                idx=0
            else:
                idx=ord(char)-ord('a')+1 #aca daria 0 para a, 1 para b, etc (ord nos devuelve el codigo numerico, entonces lo que hacemos con a resta es ej: b que es 98, seria 98-97(que es a) y te da 1)
            letras[idx].append(palabra)


    return palabras

with open("palabras.txt", "r", encoding="utf-8") as f:
    palabras = [line.strip() for line in f if line.strip()]
ordenadas = radix_sort(palabras)
print("Palabras ordenadas:")
for p in ordenadas:
    print(p)