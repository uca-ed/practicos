# Uso de ej1.py

Script del Ejercicio 1 (Árboles sobre arreglos).

## Descripción

Implementa operaciones sobre un árbol representado en un arreglo:
- **a)** Calcula la altura del árbol sin hacer recorridos (usando fórmulas matemáticas)
- **b)** Realiza un barrido pre-orden del árbol

## Representación del árbol

El árbol se representa en un arreglo donde:
- El índice 0 es la raíz
- Para un árbol de grado `d`, los hijos de un nodo en índice `i` están en: `i*d + 1, i*d + 2, ..., i*d + d`
- `None` o `0` indica una posición vacía

## Formato del archivo de entrada

```
<grado>
<valor1> <valor2> <valor3> ... <valorN>
```

Ejemplo (`arbol_ej1.txt`):
```
3
1 2 3 4 5 6 7 8 9 10 None None None
```

Este representa un árbol de grado 3 (cada nodo puede tener hasta 3 hijos).

## Ejecución básica

Desde la carpeta `03.Arboles`:

```bash
python3 ej1.py <archivo>
```

Sin flags, muestra altura y recorrido pre-orden.

## Flags

- `--altura`: Calcula y muestra la altura del árbol sin recorrido
- `--preorden`: Realiza y muestra el recorrido pre-orden

## Ejemplos

Mostrar todo (altura y pre-orden):
```bash
python3 ej1.py arbol_ej1.txt
```

Solo altura:
```bash
python3 ej1.py arbol_ej1.txt --altura
```

Solo recorrido pre-orden:
```bash
python3 ej1.py arbol_ej1.txt --preorden
```

Desde la raíz del repositorio:
```bash
python3 03.Arboles/ej1.py 03.Arboles/arbol_ej1.txt
```

## Explicación del algoritmo de altura

La altura se calcula sin recorrer el árbol usando la fórmula matemática que relaciona el índice de un nodo con su nivel. Para un árbol de grado `d`:

- Un nodo en el nivel `h` tiene índices en el rango determinado por la suma geométrica
- Dado el último índice con valor, se calcula su nivel usando: `h = floor(log_d(i * (d-1) + 1))`

Esto permite calcular la altura en O(n) para encontrar el último elemento, sin recorrer la estructura del árbol.
