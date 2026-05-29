import subprocess
import sys
import os

def ejecutar_script(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print(f"Ejecutando {nombre_archivo}")
        subprocess.run([sys.executable, nombre_archivo])
    else:
        print(f"No se encontro el archivo {nombre_archivo}")

if __name__ == "__main__":
    print("\nTRABAJO PRACTICO 1: GRAFOS")
    print("\n","*" * 50,"\n")
    scripts = ["ejercicio1.py", "ejercicio2.py", "ejercicio3.py"]
    for script in scripts:
        ejecutar_script(script)
        print("\n","*" * 50,"\n")