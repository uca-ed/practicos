
#lista de colas (voy a representar las colas en listas), una cola en cada una de las posiciones de la lista que corresponde a un elemento del alfabeto
with open('palabras.txt', 'r') as f:
    contenido = f.read()
    palabras_a_ordenar = contenido.split(',')
#print(palabras_a_ordenar)
def indice(caracter):
    return ((ord(caracter)-ord('a'))+1)
listas=[]
max_len = max(len(p) for p in palabras_a_ordenar)
for i in range(27):#creo las 26 listas vacias mas la lista por si no tiene caracter
    listas.append([])
#print(listas)
p=max_len
#print(p)
while p>=0:
    while palabras_a_ordenar:
        x=palabras_a_ordenar.pop(0)
        if p>=len(x):
            listas[0].append(x)
        else:
            listas[indice(x[p])].append(x)
    p=p-1
    for lista in listas:
        for palabra in lista:
            palabras_a_ordenar.append(palabra)
    for lista in listas:
        lista.clear()#limpio las listas para la proxima iteracion
print(palabras_a_ordenar)

