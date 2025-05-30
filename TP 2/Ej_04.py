
#Yo quiero un algoritmo que me ordene segun el prden del alfabeto, le tengo que pasar las palabras
#Ej_04

def radixSort(alfa, pal):
    pos = len(alfa) -1
    for i in reversed(alfa): #Recorre la lista al revés
        dicc = {} #Más facíl mapear con diccionarios, sorry
        for x in i: #va for palabras
            dicc[x] = [] #Clave, y le da una lista que va a funcionar como cola, por defecto
        
        #Ya hice mi diccionario, ahora tengo que mapear
        for key in dicc: #Busca las claves
            for p in pal: #Busca palabras
                if p[pos] == key:
                    dicc[key].append(p)
                    
        pos -= 1 #una posición abajo
        
        #Ahora hay que reordenar dentro de pal mismo
        aux = []
        for key in dicc:
            for value in dicc[key]:
                aux.append(value) #Agrega a una lista auxiliar
        
        pal = aux #Cambia la lista por la nueva y vuelve a comenzar con el nuevo alfabeto
    
    return pal

        
def main():
    Alfa = [(1, 3, 5, 2), ("Pica", "Basto"), (0, 1)]
    Pal = [(3, "Pica", 1), (2, "Basto", 1), (1, "Pica", 0), (1, "Basto", 0), (3, "Basto", 1)]
    print (f"print pal antes : {Pal}")
    
    Pal = radixSort(Alfa, Pal)
    
    print (f"print pal después: {Pal}")
    

main()