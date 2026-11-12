import json
#. Implementar el algoritmo de obtención de paso de un nodo a otro de un grafo. La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser una secuencia con los nodos a recorrer para recrear el paso.


#Algoritmo de Paso.
def AlgoritmoPaso(est,p_inicial,p_final):
    open = [] #lista de tuplas
    close = []
    punto_partida= ((p_inicial),None)
    open.append(punto_partida)
    while(len(open)!=0): 
        elemto_guardar=(open.pop(0))
        z=elemto_guardar[0]
        close.append(elemto_guardar)
        #print(p_final, "==", est["E"][z])
        if(str(p_final) not in (est["E"][z])):
            for w in est["E"][z]:
                bandera=False
                bandera2=False
                for i in range(len(open)):
                    if w in open[i][0]:
                        bandera=True
                for j in range(len(close)):
                    try:
                        if w in close[j][1]:
                            bandera2=True
                    except:
                        bandera=False
                if(bandera==False and bandera2==False):
                    open.append((w,z))
        else:
            close.append((p_final,z))
            break

    lista_final=[]
    if (str(p_final) not in close[-1][0]):
        print("no existe ningun paso de ",p_inicial," a ",p_final);
    else:
        
        current=p_final
        while(current!=p_inicial):
            for i in close:
                if(current == i[0]):
                    lista_final.append(i)
                    current=i[1]
    print("encontro ",len(lista_final)," pasos")
    for i in lista_final:
        print(i)

def main():
    f = open('archivosEjemplos/archivos_ej2/02.json', 'r')
    est = json.load(f)

    AlgoritmoPaso(est,est["P"][44],est["P"][20])
    
    f.close()

main()