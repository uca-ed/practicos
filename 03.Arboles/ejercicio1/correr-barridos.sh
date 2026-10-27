#!/bin/bash
python generar-arbol.py 4 10 > arbol.txt
python generar-arbol.py 2 20 > arbol-binario.txt
python altura.py 4 arbol.txt > altura.txt
python altura.py 2 arbol-binario.txt > altura-binario.txt
python barrido-pre-orden.py 4 arbol.txt > pre-orden.txt
python barrido-post-orden.py 4 arbol.txt > post-orden.txt
python barrido-por-niveles.py 4 arbol.txt > por-niveles.txt
python barrido-simetrico.py arbol-binario.txt > simetrico.txt
