import argparse
import math


class ArbolArreglo:
    """
    Árbol representado sobre un arreglo.
    Los nodos se almacenan en el arreglo donde:
    - El índice 0 es la raíz
    - Para un árbol de grado d, los hijos de un nodo en índice i están en:
      i*d + 1, i*d + 2, ..., i*d + d
    - El valor None o 0 indica posición vacía
    """
    
    def __init__(self, arreglo, grado):
        """
        Args:
            arreglo: lista de valores del árbol (None/0 indica vacío)
            grado: grado del árbol (número máximo de hijos por nodo)
        """
        self.arreglo = arreglo
        self.grado = grado
        self.n = len(arreglo)
    
    def calcular_altura_sin_recorrido(self):
        """
        Calcula la altura del árbol sin hacer recorridos.
        Usa la fórmula matemática basada en el último índice con valor.
        
        Para un árbol de grado d:
        - Nivel 0 (raíz): índice 0
        - Nivel 1: índices 1 a d
        - Nivel 2: índices d+1 a d+d²
        - Nivel h: último nodo en índice (d^(h+1) - 1) / (d - 1) - 1
        
        Returns:
            int: altura del árbol (número de niveles - 1)
        """
        # Encontrar el último índice con valor no vacío
        ultimo_idx = -1
        for i in range(self.n - 1, -1, -1):
            if self.arreglo[i] is not None and self.arreglo[i] != 0:
                ultimo_idx = i
                break
        
        if ultimo_idx == -1:
            return -1  # Árbol vacío
        
        if ultimo_idx == 0:
            return 0  # Solo raíz
        
        # Calcular el nivel del último nodo usando la fórmula inversa
        # Para un nodo en índice i, su nivel h se calcula:
        # i < (d^(h+1) - 1) / (d - 1)
        # Resolviendo: h = floor(log_d(i * (d-1) + 1))
        
        d = self.grado
        if d == 1:
            # Caso especial: árbol degenerado (lista)
            return ultimo_idx
        
        # Calculamos el nivel usando logaritmos
        altura = math.floor(math.log(ultimo_idx * (d - 1) + 1, d))
        return altura
    
    def preorden(self):
        """
        Realiza un recorrido pre-orden del árbol.
        Pre-orden: raíz, luego subárboles izquierdo a derecho.
        
        Returns:
            list: lista de valores en orden pre-orden
        """
        resultado = []
        self._preorden_recursivo(0, resultado)
        return resultado
    
    def _preorden_recursivo(self, idx, resultado):
        """
        Función auxiliar recursiva para pre-orden.
        
        Args:
            idx: índice actual en el arreglo
            resultado: lista donde se acumulan los valores
        """
        # Verificar que el índice sea válido y tenga valor
        if idx >= self.n or self.arreglo[idx] is None or self.arreglo[idx] == 0:
            return
        
        # Visitar el nodo actual (pre-orden)
        resultado.append(self.arreglo[idx])
        
        # Visitar todos los hijos
        for i in range(1, self.grado + 1):
            hijo_idx = idx * self.grado + i
            if hijo_idx < self.n:
                self._preorden_recursivo(hijo_idx, resultado)
    
    def __str__(self):
        """Representación en string del árbol."""
        return f"ArbolArreglo(grado={self.grado}, valores={self.arreglo})"


def cargar_desde_archivo(ruta):
    """
    Carga un árbol desde un archivo.
    Formato del archivo:
    - Primera línea: grado del árbol
    - Segunda línea en adelante: valores del arreglo separados por espacios
    - Use 'None' para posiciones vacías (el string '0' también se interpreta como vacío)
    
    Args:
        ruta: ruta al archivo
        
    Returns:
        ArbolArreglo: el árbol cargado
    
    Raises:
        FileNotFoundError: si el archivo no existe
        ValueError: si el formato del archivo es inválido
    """
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{ruta}' no fue encontrado")
    
    if len(lineas) < 2:
        raise ValueError("El archivo debe tener al menos 2 líneas (grado y valores)")
    
    # Leer grado
    grado = int(lineas[0].strip())
    
    # Leer valores del arreglo
    valores_str = ' '.join(lineas[1:]).split()
    arreglo = []
    for v in valores_str:
        v = v.strip()
        # Nota: '0' se interpreta como posición vacía, no como el valor cero
        # Si necesita representar el valor 0, use otro formato o modifique esta lógica
        if v.lower() == 'none' or v == '0':
            arreglo.append(None)
        else:
            try:
                arreglo.append(int(v))
            except ValueError:
                arreglo.append(v)
    
    return ArbolArreglo(arreglo, grado)


def main():
    parser = argparse.ArgumentParser(
        description='Ejercicio 1 - Árboles sobre arreglos'
    )
    parser.add_argument('archivo', help='Ruta al archivo con el árbol')
    parser.add_argument('--altura', action='store_true',
                       help='Calcular altura sin recorrido')
    parser.add_argument('--preorden', action='store_true',
                       help='Realizar recorrido pre-orden')
    
    args = parser.parse_args()
    
    # Cargar el árbol
    arbol = cargar_desde_archivo(args.archivo)
    
    hizo_algo = False
    
    if args.altura:
        altura = arbol.calcular_altura_sin_recorrido()
        print(f'Altura del árbol: {altura}')
        hizo_algo = True
    
    if args.preorden:
        recorrido = arbol.preorden()
        print(f'Recorrido pre-orden: {" ".join(map(str, recorrido))}')
        hizo_algo = True
    
    if not hizo_algo:
        # Por defecto muestra ambos
        altura = arbol.calcular_altura_sin_recorrido()
        recorrido = arbol.preorden()
        print(f'Altura del árbol: {altura}')
        print(f'Recorrido pre-orden: {" ".join(map(str, recorrido))}')


if __name__ == '__main__':
    main()
