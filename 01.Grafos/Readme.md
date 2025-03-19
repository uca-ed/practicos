# Ejercicios sobre Grafos

1. Representar a un grafo utilizando una matriz de adyacencia. Sobre tal representación, se debe poder ejecutar los siguientes operadores:

      a. Minimales del grafo  
      b. Maximales del grafo  
      c. Vecindad derecha de un nodo  
      d. Vecindad izquierda de un nodo  

   Los grafos se deben poder leer de los archivos provistos como ejemplo; hay dos formatos usados: 
     * csv mostrando la matriz (se deberán identificar a los nodos según la posición que tengan en la misma)
     * json con la estructura del grafo

>  Utilizar los archivos provistos en el archivo archivos_ej1.zip 

2. Verificar si un grafo dado cumple las propiedades de Reflexividad, Simetría, Antisimetría y Transitividad. Luego, debe decidir si el grafo es un orden o es corresponde a una relación de equivalencia.

>  Utilizar los archivos provistos en el directorio archivos_ej2.zip 

3. Implementar el algoritmo de obtención de paso de un nodo a otro de un grafo. La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser una secuencia con los nodos a recorrer para recrear el paso.

>  Utilizar los archivos provistos en el directorio archivos_ej3.zip 

Nota: Los archivos json pueden leerse con el siguiente código python:  

```
import json
f = open('ed.json')
estructura = json.load(f)

# Imprimo los nodos que tienen vecindad derecha
for i in estructura['E']:
    print(i)

# Imprimo la vecindad derecha de a
print (estructura['E']['a'])

# Imprimo la cardinalidad derecha de a
print (len(estructura['E']['a']))

f.close()
```
