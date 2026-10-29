#!/bin/bash
python generar-arbol.py 4 10 > arbol.txt
python generar-arbol.py 2 20 > arbol-binario.txt
python ejercicio_1b.py 4 arbol.txt > pre-orden.txt
python ejercicio_1c.py 4 arbol.txt > post-orden.txt
python ejercicio_1d.py 4 arbol.txt > por-niveles.txt
python ejercicio_1e.py arbol-binario.txt > simetrico.txt
