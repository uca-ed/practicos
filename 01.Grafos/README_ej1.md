# Uso de ej1.py

Script del Ejercicio 1 (grafos con matriz de adyacencia).

## Ejecución básica

Desde la carpeta `01.Grafos`:

```
python3 ej1.py <archivo>
```

Si no se pasan flags muestra minimales y maximales.

## Flags

- `--minimales`  muestra nodos con indegree = 0
- `--maximales`  muestra nodos con outdegree = 0
- `--vec-der NODO` vecindad derecha de NODO
- `--vec-izq NODO` vecindad izquierda de NODO

## Ejemplos

Minimales desde CSV:
```
python3 ej1.py archivos_ej1/01.csv --minimales
```

Maximales desde JSON:
```
python3 ej1.py archivos_ej1/01.json --maximales
```

Vecindad derecha del nodo 2:
```
python3 ej1.py archivos_ej1/01.json --vec-der 2
```

Vecindad izquierda del nodo 10:
```
python3 ej1.py archivos_ej1/01.json --vec-izq 10
```

Varias operaciones juntas:
```
python3 ej1.py archivos_ej1/01.json --minimales --maximales --vec-der 3
```

Desde la raíz del repo:
```
python3 01.Grafos/ej1.py 01.Grafos/archivos_ej1/01.csv --minimales
```
