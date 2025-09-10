# Uso de ej2.py

Script del Ejercicio 2 (propiedades de una relación sobre un conjunto P).

## Ejecución básica

Desde la carpeta `01.Grafos`:

```
python3 ej2.py <archivo.json>
```

Si no se pasan flags evalúa todas las propiedades y muestra una clasificación (equivalencia / orden parcial / ninguna).

## Flags

- `--reflexiva`        chequea solo reflexividad
- `--simetrica`        chequea solo simetría
- `--antisimetrica`    chequea solo antisimetría
- `--transitiva`       chequea solo transitividad
- `--detalles`         muestra ejemplos concretos de fallos (limitados para no saturar)

(Se pueden combinar varios; si se pasa al menos uno, solo se muestran esos.)

## Formato de entrada

JSON con dos claves:
- `P`: lista de nodos (strings)
- `E`: diccionario nodo -> lista de sucesores (pares (nodo, sucesor) pertenecen a la relación)

Ejemplo mínimo:
```
{
  "P": ["a", "b"],
  "E": {"a": ["a", "b"], "b": ["b"]}
}
```

## Ejemplos

Chequear todo (todas las propiedades + clasificación):
```
python3 ej2.py archivos_ej2/01.json
```

Solo reflexividad y transitividad con detalles:
```
python3 ej2.py archivos_ej2/01.json --reflexiva --transitiva --detalles
```

Ver simetría únicamente:
```
python3 ej2.py archivos_ej2/02.json --simetrica
```

Desde la raíz del repo:
```
python3 01.Grafos/ej2.py 01.Grafos/archivos_ej2/01.json --detalles
```

## Salida típica
```
Reflexiva: Sí
Simétrica: No
Antisimétrica: Sí
Transitiva: Sí
Clasificación: Orden parcial
```

Con `--detalles` y una transgresión de transitividad mostrará ejemplos `(x,y,z)` donde falta `(x,z)`.
