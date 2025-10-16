import csv

def radixSortABC(lista):   
    numeroMaximoDeLetras = 0
    separadoPorLetra = []
    for palabra in lista:
        w = []
        for l in palabra.upper():
            w.append(l)
        word = {"palabra":palabra,"letras":w,"n":len(w)}
        separadoPorLetra.append(word)
        if len(w) > numeroMaximoDeLetras:
            numeroMaximoDeLetras = len(w)
    
    #for p in separadoPorLetra:        
    #    print(p)
    #print(f"numero maximo de letras: {numeroMaximoDeLetras}")

    for palabra in separadoPorLetra:
        espaciosEnBlanco = numeroMaximoDeLetras - palabra["n"]
        for i in range(espaciosEnBlanco):
            palabra["letras"].append(" ")

    #for p in separadoPorLetra:        
    #    print(p)
    
    #print("A"<"B") # True
    #print("B">"C") # False
    #print(" "<"A") # True
    
    colasDeOrdenado = []
    for L in " ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        colasDeOrdenado.append({"letra":L,"cola":[]})
    
    for i in range(numeroMaximoDeLetras):
        #######
        #print(f"\n----paso: {i}----")
        #for palabra in separadoPorLetra:
        #    print(f"   {palabra["letras"]}---")
        #######
        for palabra in separadoPorLetra:          
            letra = palabra["letras"][numeroMaximoDeLetras - i - 1]
            #print(letra)
            for L in colasDeOrdenado:
                if L["letra"] == letra:
                    L["cola"].append(palabra)            
            
        separadoPorLetra.clear()
        for L in colasDeOrdenado:
            for p in L["cola"]:
                separadoPorLetra.append(p)
            L["cola"].clear()
        
        
    listaOrdenada = []
    for p in separadoPorLetra:
        listaOrdenada.append(p["palabra"])
        
    return listaOrdenada
    
    


def main():
    with open('datos.csv', newline='') as archivo_csv:
        lista = []
        lector_csv = csv.reader(archivo_csv)
        for palabra in list(lector_csv): # una lista de python con 
            lista.append(palabra[0])
        ordenada = radixSortABC(lista)
        
        print(f"\nlista desordenada: {lista}")
        print(f"\nradix sort:        {ordenada}")
        print()
        
        
print("Ejercicio 4 - Radiz sort\n")
main()