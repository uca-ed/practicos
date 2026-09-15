# Estructuras Lineales

1. Representar colas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre colas y operar, partiendo de una cola vacía. Se debe mostrar el resultado final.

> [!TIP] 
> El archivo puede ser del estilo
> 
> ```
> ENQUEUE,1
> ENQUEUE,2
> ENQUEUE,3
> ENQUEUE,4
> DEQUEUE,
> DEQUEUE,
> ```


2. Representar pilas sobre un arreglo. El algoritmo debe leer el archivo de operaciones sobre pilas y operar, partiendo de una pila vacía. Se debe mostrar el resultado final.  

> [!TIP] 
> El archivo puede ser del estilo
> 
> ```
> PUSH,1
> PUSH,2
> PUSH,3
> POP,
> POP,
> ```

3. Representar listas por medio de celdas con enlace simple.  

4. Implementar Radix Sort y ordenar las palabras de los archivos indicados.  

5. Implementar en un lenguaje de programación el algoritmo de cálculo de T-Sort basado en un grafo. De no ser posible calcularlo, indicar que la estructura es cíclica.  
  
> [!NOTE] 
> La aplicación debe soportar leer el grafo desde un archivo de disco y la salida debe ser la secuencia generada por t-sort.   

6. Se modeliza en un arreglo “INSCRIPTOS” de 5 dimensiones la cantidad de alumnos que hay en las aulas de la universidad en cada bloque horario (según las listas de inscripción).  

A tal fin, se organiza el arreglo en 5 dimensiones:  

    d0: edificio (4 edificios)  
    d1: piso (5 pisos por edificio)  
    d2: ala (norte o sur)  
    d3: aula (25 aulas por ala)  
    d4: bloque horario (85 - 17 bloques horarios por 5 días)  
  
  
También se guarda un arreglo de similares características “CAPACIDAD” para guardar la capacidad de cada una de las aulas. Dado que es dato el vector de dimensiones, se quiere representar a los arreglos de 5 dimensiones sobre arreglos de única dimensión.  

**Implementar:**   

* Creación de las estructuras   
* Carga de datos en las mismas  

Dar algoritmos que respondan los siguientes interrogantes:   
a. Cuál es el aula/bloque horario con mayor porcentaje de ocupación   

b. Promedio de alumnos por piso en un bloque horario pasado como parámetro (entre todos los edificios – sólo 5 promedios)  

c. Dado como parámetro el edificio, el piso y el bloque horario, devolver la cantidad total de alumnos que están presentes en cada ala.  

> [!TIP] 
> Los algoritmos deberían trabajar sobre la estructura de representación, es decir el arreglo lineal. 
> De ser posible, la algoritmia debería contemplar la situación e iterar no sobre múltiples índices, sino sobre los índices del arreglo lineal que correspondan, según la fórmula general.   
> 
> Como no se provee un archivo de datos, se deben también generar datos para las dimensiones requeridas.

7. Implementar Sort topológico sobre un grafo dado como dato en un archivo.  
