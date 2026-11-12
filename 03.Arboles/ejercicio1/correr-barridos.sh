#!/bin/bash
python generar-arbol.py 4 10 > arbol.txt
python generar-arbol.py 2 20 > arbol-binario.txt
python barrido-pre-orden.py 4 arbol.txt > pre-orden.txt
python barrido-post-orden.py 4 arbol.txt > post-orden.txt
python barrido-por-nievles.py 4 arbol.txt > por-niveles.txt
python barrido-simetrico.py arbol-binario.txt > simetrico.txt
