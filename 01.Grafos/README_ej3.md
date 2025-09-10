# Uso de ej3.py

Script del Ejercicio 3: obtener un camino ("paso") entre dos nodos de un grafo dirigido.

## Ejecución básica

Desde `01.Grafos`:
```
python3 ej3.py <archivo.json> <origen> <destino>
```
Devuelve una secuencia de nodos (si existe) usando BFS (camino con menor número de aristas).

## Flags
- `--alg bfs|dfs`  Algoritmo a usar (por defecto `bfs`). `dfs` devuelve algún camino, no necesariamente mínimo.
- `--solo-longitud`  Muestra solo la longitud (en aristas) del camino encontrado.

Si no hay camino se imprime `No existe camino`.

## Formato de entrada
Igual a ejercicios anteriores: JSON con
- `P`: lista de nodos (strings)
- `E`: diccionario nodo -> lista de sucesores

## Ejemplos
Camino mínimo de 1 a 50:
```
python3 ej3.py archivos_ej3/esDivisorDe-200.json 1 50
```

Solo la longitud entre 2 y 96:
```
python3 ej3.py archivos_ej3/esDivisorDe-200.json 2 96 --solo-longitud
```

Usar DFS (puede dar un camino distinto al mínimo):
```
python3 ej3.py archivos_ej3/esDivisorDe-200.json 1 99 --alg dfs
```

Desde la raíz del repo:
```
python3 01.Grafos/ej3.py 01.Grafos/archivos_ej3/esDivisorDe-200.json 1 180
```

## Notas
- BFS garantiza mínima cantidad de aristas.
- Si origen=destino se devuelve ese único nodo.
