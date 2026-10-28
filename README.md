# UCA - Estructuras de Datos

Este repositorio contiene enunciados para los trabajos prácticos de implementación que se pedirán durante la cursada de Estructuras de Datos.

# Instrucciones para la Entrega de Trabajos Prácticos

La entrega de los trabajos prácticos es **grupal**. Para eso, usar la cuenta de GitHub de **uno de los miembros del equipo** durante toda la cursada.

## Pasos para la entrega

### 1. Realizar un fork del repositorio  
Cada equipo debe realizar un **fork** de este repositorio. Luego de este paso, el repositorio aparecerá en la cuenta de GitHub del usuario que hizo el fork.  
![image](https://github.com/user-attachments/assets/88dbbe3d-2ed0-4b4d-977a-e451f7229dca)

### 2. Agregar colaboradores  
Desde la cuenta que realizó el fork, configurar como **colaboradores** a los demás miembros del equipo. Para eso:
   - Ir a la configuración del repositorio en GitHub.

  ![image](https://github.com/user-attachments/assets/3a6b1da9-2622-4504-abd1-ac4cfd52864d)

  ![image](https://github.com/user-attachments/assets/aaec82a8-d9e3-456d-828e-aaf9025b9ffa)
  
  ![image](https://github.com/user-attachments/assets/6434a210-0107-48d5-86ab-558eed88bbf1
  
   - Agregar los nombres de usuario de los integrantes del equipo.

  ![image](https://github.com/user-attachments/assets/8ff27756-eba9-4f13-becc-e1eccd2e875f)

### 3. Trabajar en el repositorio  
Luego de este paso, todos los miembros del equipo pueden acceder al repositorio y trabajar en el mismo.  
Cada ejercicio del práctico debe estar resuelto en un archivo independiente y deben estar situados en cada unidad. Por ejemplo:

```
.
├── 01.Grafos
│   ├── ejercicio1.py
│   ├── ejercicio2.py
│   ├── ejercicio3.py
│   └── Readme.md
├── 02.EstructurasLineales
│   └── Readme.md

```

### 3.1. Archivos de datos
Los ejercicios deben poder ejecutarse utilizando los archivos de datos provistos en el repositorio, pero pueden también agregar archivos propios.  

En caso de que los archivos de ejemplo no sean provistos, cada equipo puede preparar sus archivos y sumarlos al Pull Request.  

### 4. Enviar el enlace del repositorio  
Compartir el **link del repositorio** con el docente.

### 5. Realizar un **Pull Request** para la entrega  
Cuando el trabajo práctico esté listo para su entrega:
   - Crear un **Pull Request** en GitHub. El nombre del Pull Request debe contener los apellidos de los alumnos que participan en el grupo.

  ![image](https://github.com/user-attachments/assets/307f2593-91c2-41fc-b0f7-902e9bebc133)

  ![image](https://github.com/user-attachments/assets/8081d5a3-a7cd-4327-a6b2-1cba83abf056)

   - Comparar la branch donde se realizo el trabajo a entregar con la branch "Main" y crear el Pull Request

  ![image](https://github.com/user-attachments/assets/69494c47-fced-4f7d-81e9-e6e65091d2c5)

   - Especificar el trabajo pratico que se esta entregando, indicando los nombres de los participantes y crear el Pull Request

  ![image](https://github.com/user-attachments/assets/47796d26-1256-4cb5-b956-f18d7761e5ea)

   - Notificar al docente sobre la entrega.
# TP Estructuras Lineales

Implementación en Python, un archivo por ejercicio. Cada script se puede
ejecutar directamente (`python3 ejN_....py`); todos leen por defecto un
archivo de ejemplo en `data/`, y opcionalmente aceptan la ruta a otro
archivo como argumento (`python3 ej1_colas.py data/otro_archivo.txt`).

## Contenido

| Archivo | Ejercicio | Descripción |
|---|---|---|
| `ej1_colas.py` | 1 | Cola sobre arreglo circular. Lee `data/operaciones_cola.txt`. |
| `ej2_pilas.py` | 2 | Pila sobre arreglo. Lee `data/operaciones_pila.txt`. |
| `ej3_lista_enlazada.py` | 3 | Lista con celdas de enlace simple (Nodo + ListaEnlazada). |
| `ej4_radix_sort.py` | 4 | Radix Sort LSD sobre palabras. Lee `data/palabras.txt`. |
| `ej5_tsort.py` | 5 | T-Sort por eliminación de nodos fuente (grado de entrada). Lee `data/grafo_tsort.txt`. |
| `ej6_inscriptos.py` | 6 | Arreglo 5D (INSCRIPTOS/CAPACIDAD) sobre arreglo lineal, con `h` y `h⁻¹`. |
| `ej7_sort_topologico.py` | 7 | Sort topológico con DFS. Lee `data/grafo_topologico.txt`. |

También hay `data/grafo_ciclico.txt` para probar la detección de ciclos
(pasalo como argumento a `ej5_tsort.py` o `ej7_sort_topologico.py`).

## Notas por ejercicio

**Ej. 1 y 2 (cola/pila):** el "arreglo" es un `list` de Python de
capacidad fija (`capacidad=100` por defecto), usado como estructura de
tamaño fijo real (no se usa `append`/`pop` de Python como atajo): la cola
usa punteros `frente`/`fondo` circulares, la pila un puntero `tope`.

**Ej. 4 (Radix Sort):** sigue el algoritmo de la cátedra tal cual está en
la diapositiva: procesa desde la posición **menos significativa** (el
último carácter, j=1) hacia la más significativa (primer carácter, j=p),
usando 27 baldes (0 para relleno, 1-26 para 'a'-'z'). Esto hace que las
palabras más cortas se traten como si tuvieran "ceros" (relleno) a la
**izquierda**, igual que un número — por eso el resultado **no** es el
mismo que un `sorted()` alfabético común (por ejemplo, "pila" puede
quedar antes que "arbol", porque se comparan primero los últimos
caracteres). Es el comportamiento esperado del algoritmo tal como está
definido, no un bug.

**Ej. 5 vs Ej. 7:** son dos algoritmos distintos para el mismo tipo de
problema, para mostrar dos enfoques: el 5 elimina iterativamente nodos
fuente (grado de entrada 0, en línea con `Min(G)`); el 7 usa DFS con
postorden invertido. Ambos detectan ciclos.

**Ej. 6 (INSCRIPTOS):** como no se da un archivo de datos, se generan
datos aleatorios (`seed=42` para reproducibilidad). Las consultas b) y c)
recorren el arreglo lineal directamente con los saltos (strides) que
salen de la fórmula de `h`, sin reconstruir los 5 índices en cada paso,
tal como pide la consigna.
