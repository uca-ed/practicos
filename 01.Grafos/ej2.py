import argparse
import json
from typing import Dict, List, Set, Tuple


class Relacion:
    """Representa una relación binaria R sobre un conjunto P.

    Guardamos:
      - lista de nodos (dominio) en el orden provisto
      - para cada nodo: conjunto de sucesores (vecindad derecha) para O(1) en membership
    """

    def __init__(self, nodos: List[str]):
        self.nodos: List[str] = nodos
        self.idx: Dict[str, int] = {v: i for i, v in enumerate(nodos)}
        self.sucesores: List[Set[str]] = [set() for _ in nodos]

    def agregar(self, a: str, b: str):
        if a in self.idx and b in self.idx:
            self.sucesores[self.idx[a]].add(b)

    @staticmethod
    def cargar_json(path: str) -> "Relacion":
        with open(path) as f:
            data = json.load(f)
        nodos = data["P"]
        r = Relacion(nodos)
        for a, lista in data.get("E", {}).items():
            for b in lista:
                r.agregar(a, b)
        return r

    # --- Chequeos de propiedades ---
    # Cada método implementa directamente la definición lógica.

    def es_reflexiva(self) -> Tuple[bool, List[str]]:
        """Reflexiva: ∀x∈P, (x,x)∈R.
        Devuelve (bool, faltantes) para mostrar qué pares faltan si falla."""
        faltan = [x for x in self.nodos if x not in self.sucesores[self.idx[x]]]
        return (len(faltan) == 0, faltan)

    def es_simetrica(self) -> Tuple[bool, List[Tuple[str, str]]]:
        """Simétrica: ∀(x,y)∈R ⇒ (y,x)∈R.
        Recorremos cada arista (x,y) y verificamos su 'arista espejo'."""
        faltan = []
        for i, x in enumerate(self.nodos):
            for y in self.sucesores[i]:
                # (x,x) no requiere chequeo extra; su simétrica es sí misma
                if y != x:
                    if x not in self.sucesores[self.idx[y]]:
                        faltan.append((y, x))  # par espejo ausente
        return (len(faltan) == 0, faltan)

    def es_antisimetrica(self) -> Tuple[bool, List[Tuple[str, str]]]:
        """Antisimétrica: ∀(x,y),(y,x)∈R con x≠y ⇒ x=y (o sea no deben existir tales pares distintos).
        En práctica: buscamos pares (x,y) con x<y (para no duplicar) donde ambos sentidos existan."""
        violaciones = []
        for i, x in enumerate(self.nodos):
            for y in self.sucesores[i]:
                if y != x:  # ignorar la diagonal
                    if x in self.sucesores[self.idx[y]]:  # ambos sentidos presentes
                        # Ordenamos para reportar consistente
                        if self.idx[y] > i:  # reportar solo una vez (x,y) con idx(x)<idx(y)
                            violaciones.append((x, y))
        return (len(violaciones) == 0, violaciones)

    def es_transitiva(self) -> Tuple[bool, List[Tuple[str, str, str]]]:
        """Transitiva: ∀(x,y),(y,z)∈R ⇒ (x,z)∈R.
        Idea práctica: para cada x y cada y∈R(x), comprobamos que sucesores(y)⊆sucesores(x).
        Si falta algún (x,z) lo registramos como violación (x,y,z).
        Nota: Esto es costoso en el peor caso; se corta temprano si encuentra demasiadas violaciones."""
        violaciones = []
        # Heurística: detener tras cierto número para no explotar salida (en conjunto grande)
        MAX_VIOLACIONES = 20
        for i, x in enumerate(self.nodos):
            suc_x = self.sucesores[i]
            for y in suc_x:
                suc_y = self.sucesores[self.idx[y]]
                # Chequeo por diferencia: si hay z en suc_y no en suc_x => violación (x,y,z)
                diff = suc_y - suc_x
                for z in diff:
                    violaciones.append((x, y, z))
                    if len(violaciones) >= MAX_VIOLACIONES:
                        return (False, violaciones)
        return (len(violaciones) == 0, violaciones)


def clasificacion(reflexiva: bool, simetrica: bool, antisimetrica: bool, transitiva: bool) -> str:
    """Devuelve etiqueta básica según combinación de propiedades."""
    if reflexiva and simetrica and transitiva:
        return "Relación de equivalencia"
    if reflexiva and antisimetrica and transitiva:
        return "Orden parcial"  # (no distinguimos aquí si es total)
    return "Ninguna de las anteriores"


def main():
    parser = argparse.ArgumentParser(description="Ejercicio 2 - Propiedades de una relación")
    parser.add_argument('archivo', help='Ruta a archivo JSON con P y E')
    parser.add_argument('--reflexiva', action='store_true')
    parser.add_argument('--simetrica', action='store_true')
    parser.add_argument('--antisimetrica', action='store_true')
    parser.add_argument('--transitiva', action='store_true')
    parser.add_argument('--detalles', action='store_true', help='Muestra ejemplos de fallos')
    args = parser.parse_args()

    rel = Relacion.cargar_json(args.archivo)

    # Si no se piden flags individuales, evaluamos todas.
    evaluar_todas = not (args.reflexiva or args.simetrica or args.antisimetrica or args.transitiva)

    resultados = {}

    if args.reflexiva or evaluar_todas:
        ok, faltan = rel.es_reflexiva()
        resultados['Reflexiva'] = (ok, faltan)
    if args.simetrica or evaluar_todas:
        ok, faltan = rel.es_simetrica()
        resultados['Simétrica'] = (ok, faltan)
    if args.antisimetrica or evaluar_todas:
        ok, viol = rel.es_antisimetrica()
        resultados['Antisimétrica'] = (ok, viol)
    if args.transitiva or evaluar_todas:
        ok, viol = rel.es_transitiva()
        resultados['Transitiva'] = (ok, viol)

    # Salida
    for nombre, (ok, data) in resultados.items():
        print(f"{nombre}: {'Sí' if ok else 'No'}")
        if args.detalles and not ok:
            if nombre == 'Reflexiva':
                print('  Faltan bucles:', ', '.join(data[:20]), '...' if len(data) > 20 else '')
            elif nombre == 'Simétrica':
                print('  Faltan pares espejo:', ', '.join(f"({a},{b})" for a, b in data[:10]), '...' if len(data) > 10 else '')
            elif nombre == 'Antisimétrica':
                print('  Pares que violan:', ', '.join(f"({a},{b})" for a, b in data[:10]), '...' if len(data) > 10 else '')
            elif nombre == 'Transitiva':
                print('  Ejemplos (x,y,z) donde falta (x,z):', ', '.join(f"({x},{y},{z})" for x, y, z in data[:6]), '...' if len(data) > 6 else '')

    if evaluar_todas:
        ref = resultados['Reflexiva'][0]
        sim = resultados['Simétrica'][0]
        anti = resultados['Antisimétrica'][0]
        tra = resultados['Transitiva'][0]
        print('Clasificación:', clasificacion(ref, sim, anti, tra))


if __name__ == '__main__':
    main()
