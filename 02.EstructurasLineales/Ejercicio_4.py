def rearmar_buckets_en_orden(keys_dict):
    return {k: [] for k in sorted(keys_dict.keys())}

def radix_sort(textos):
    if not textos:
        return textos

    ancho = max(len(t) for t in textos)
    trabajo = [t.ljust(ancho) for t in textos]

    for col in range(ancho - 1, -1, -1):
        print(f"[columna {col}]")
        vistos = {}
        for palabra in trabajo:
            c = palabra[col]
            if c not in vistos:
                vistos[c] = None
                print(f"  - visto símbolo: {repr(c)}")

        buckets = rearmar_buckets_en_orden(vistos)
        print(f"  buckets en orden: {list(buckets.keys())}")

        for palabra in trabajo:
            buckets[palabra[col]].append(palabra)

        trabajo = []
        for k in buckets:
            trabajo.extend(buckets[k])
            print(f"    {repr(k)} → {buckets[k]}")

    return [t.rstrip() for t in trabajo]

def main():
    palabras = [
        "C21", "B33", "A11", "A21", "B12", "C11", "A12", "B21"
    ]

    print("== ENTRADA ==")
    print(palabras)

    resultado = radix_sort(palabras)

    print("\n== ORDENADAS ==")
    for p in resultado:
        print(p)

if __name__ == "__main__":
    main()
