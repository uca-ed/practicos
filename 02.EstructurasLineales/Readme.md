# Estructuras Lineales

1. Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. Se debe mostrar el resultado final.

2. Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. Se debe mostrar el resultado final.

3. Representar listas por medio de celdas con enlace simple.

4. Implementar Radix Sort y ordenar las palabras de los archivos indicados.

5. Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. De no ser posible calcularlo, indicar que la estructura es cíclica.

La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser una secuencia con los nodos a recorrer para recrear el paso.

6. Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).

A tal fin, se organiza el arreglo en 5 dimensiones:

d0: edificio (4 edificios)
d1: piso (5 pisos por edificio) 
d2: ala (norte o sur) 
d3: aula (25 aulas por ala) 
d4: bloque horario (85 - 17 bloques horarios por 5 días) 


También se guarda un arreglo de similares características “CAPACIDAD” para guardar la capacidad de cada una de las aulas. Dado que es dato el vector de dimensiones, se quiere representar a los arreglos de 5 dimensiones sobre arreglos de única dimensión.

 Implementar: 

Creación de las estructuras 
Carga de datos en las mismas 
Dar algoritmos que respondan los siguientes interrogantes 
a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación 

b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios) 

c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala. 


Las pruebas deben también generar datos para las dimensiones requeridas 
Informe comparando los tiempos de respuesta de ambos desarrollos, tanto en forma tabular como gráficamente

7. Implementar Sort topológico sobre un grafo dado como dato en un archivo.
