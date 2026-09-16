import string

def main():

    with open("palabras.csv", "r") as f:
        datos = f.read()

    palabras=datos.split(",")
    max=0
    for palabra in palabras:
        if max<len(palabra):
            max=len(palabra)

    p=max
    r=27
    for i in range(p):
        lista_chicas=[]
        dic = {letra: [] for letra in string.ascii_lowercase}
        for palabra in palabras:
            try:
                indice=palabra[p-1-i]
                print(indice)
                if indice not in dic.keys():
                    print("error")
                else:
                    dic[indice].append(palabra)
            except:
                lista_chicas.append(palabra)
            

        palabras=[]
        for palabra in lista_chicas:
            palabras.append(palabra)
        for letras in dic:
            for palabra in dic[letras]:
                palabras.append(palabra)
        print(palabras)

    print("orden final")
    print(palabras)
main()