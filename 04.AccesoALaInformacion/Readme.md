# Acceso a la información

1. Hashing Abierto

Implementar una tabla de hashing tal que dados los datos en un archivo csv, soporte búsquedas según hashing abierto. 
Una vez creada la tabla de hashing con los datos provistos, graficar el tamaño de bucket por cada posición del arreglo.

[!NOTE]
Los archivos para trabajar con Hashing pueden ser descargados desde [el gist Unidad 4](https://gist.github.com/uca-ed/a2cf9eabc03a363c1c279fa1020f43f1.js)


2. Hashing Cerrado

Implementar una tabla de hashing tal que dados los datos en un archivo csv, soporte la búsqueda según hashing cerrado.
Generar una tabla que por cada valor provisto, indique la cantidad de veces que se calcula re-hash

3. Hashing Cerrado

Proponer para el ejercicio anterior volcar la tabla de hashing a disco y hacer las operaciones directamente en memoria secundaria.

2. Búsqueda por interpolación

Implementar búsqueda binaria y por interpolación en un arreglo de números separados uniformemente. Graficar resultados y comparar.  



[!INFO]
> Los archivos de esta unidad fueron creados
> 
> U04_nombres.csv - es un archivo de nombres tiene 14333 nombres en > castellano para utilizar en una tabla de hashing, generado a partir del siguiente código:
> 
> ```
> from names_dataset import NameDataset, NameWrapper
> 
> nd = NameDataset()
> nombres = nd.get_top_names(n=50000, country_alpha2='AR')
> 
> todos = nombres['AR']['F'] + nombres['AR']['M']
> 
> with open("U04_nombres.csv", 'w') as file:
>     for nombre in todos:
>         file.write(str(nombre) + '\n') 
> ```
> 
> U04_nombres_ingles.csv - es un archivo de 18995 nombres en inglés para utilizar en una tabla de hashing, generaos con un código similar al anterior, pero utilizando country_alpha2='US'.
> 
> Referencia: https://github.com/philipperemy/name-dataset/tree/master
