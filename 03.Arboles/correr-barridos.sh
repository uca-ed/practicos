#!/bin/bash
# Usa python3 si está (Linux/WSL/Mac) y si no, python
PY=$(command -v python3 || command -v python)
$PY generar-arbol.py 4 10 > arbol.txt
$PY generar-arbol.py 2 20 > arbol-binario.txt
$PY barrido-pre-orden.py 4 arbol.txt > pre-orden.txt
$PY barrido-post-orden.py 4 arbol.txt > post-orden.txt
$PY barrido-por-niveles.py 4 arbol.txt > por-niveles.txt
$PY barrido-simetrico.py arbol-binario.txt > simetrico.txt
$PY altura.py 4 arbol.txt > altura.txt
$PY arbol-avl.py datos-avl.txt > avl.txt
