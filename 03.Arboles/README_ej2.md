# Uso de ej2.py

Script del Ejercicio 2 (Árbol AVL).

## Descripción

Implementa un árbol AVL (Adelson-Velsky y Landis) que:
- Realiza inserciones desde un archivo de datos
- Mantiene el árbol balanceado automáticamente
- Soporta rotaciones simples y dobles para mantener el balance

## ¿Qué es un árbol AVL?

Un árbol AVL es un árbol binario de búsqueda auto-balanceado donde la diferencia de alturas entre los subárboles izquierdo y derecho de cualquier nodo es como máximo 1. Esto garantiza operaciones de búsqueda, inserción y eliminación en tiempo O(log n).

## Formato del archivo de entrada

El archivo debe contener valores numéricos separados por espacios o saltos de línea.

Ejemplo (`avl_ej2.txt`):
```
10 20 30 40 50 25
```

También puede estar en múltiples líneas:
```
10
20
30
40
50
25
```

## Ejecución básica

Desde la carpeta `03.Arboles`:

```bash
python3 ej2.py <archivo>
```

Sin flags, muestra la estructura completa del árbol, altura y recorridos.

## Flags

- `--mostrar`: Muestra la estructura visual del árbol (con alturas y balances)
- `--altura`: Muestra la altura del árbol
- `--inorden`: Muestra el recorrido in-orden (valores ordenados ascendentemente)
- `--preorden`: Muestra el recorrido pre-orden

## Ejemplos

Mostrar todo (estructura, altura y recorridos):
```bash
python3 ej2.py avl_ej2.txt
```

Solo la estructura del árbol:
```bash
python3 ej2.py avl_ej2.txt --mostrar
```

Solo la altura:
```bash
python3 ej2.py avl_ej2.txt --altura
```

Solo recorrido in-orden:
```bash
python3 ej2.py avl_ej2.txt --inorden
```

Múltiples opciones:
```bash
python3 ej2.py avl_ej2.txt --altura --inorden --preorden
```

Desde la raíz del repositorio:
```bash
python3 03.Arboles/ej2.py 03.Arboles/avl_ej2.txt
```

## Salida de ejemplo

```
Insertando 6 valores: [10, 20, 30, 40, 50, 25]

Estructura del árbol AVL:
(h=altura, b=balance)
R: 30 (h=3, b=0)
    I: 20 (h=2, b=0)
        I: 10 (h=1, b=0)
        D: 25 (h=1, b=0)
    D: 40 (h=2, b=-1)
        I: None
        D: 50 (h=1, b=0)

Altura del árbol: 3
Recorrido in-orden: 10 20 25 30 40 50
Recorrido pre-orden: 30 20 10 25 40 50
```

## Notas sobre el balance

- **Balance = altura(izq) - altura(der)**
- Balance = 0: perfectamente balanceado
- Balance = 1: subárbol izquierdo es 1 nivel más alto
- Balance = -1: subárbol derecho es 1 nivel más alto
- Si |balance| > 1, se requiere rotación (el algoritmo lo hace automáticamente)

## Rotaciones implementadas

1. **Rotación simple derecha**: caso Izquierda-Izquierda
2. **Rotación simple izquierda**: caso Derecha-Derecha
3. **Rotación doble izquierda-derecha**: caso Izquierda-Derecha
4. **Rotación doble derecha-izquierda**: caso Derecha-Izquierda
