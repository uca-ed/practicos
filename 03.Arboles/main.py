from avl import ArbolAVL

def main():
    print("=== DEMO ÁRBOL AVL ===")

    # Crear árbol vacío
    arbol = ArbolAVL()

    # Secuencia de inserciones que genera rotaciones
    datos = [50, 40, 30, 20, 10, 60, 70, 80, 90, 100]

    print(f"Inserciones: {datos}\n")

    for valor in datos:
        arbol.insertar(valor)
        print(f"\nDespués de insertar {valor}:")
        arbol.pretty_print()
        print("-" * 40)

    # Recorridos
    print("\n=== RECORRIDOS ===")
    print("Preorden:", arbol.preorder())
    print("Inorden :", arbol.inorder())

    # Altura final
    if arbol.raiz:
        print(f"Altura final del árbol: {arbol.raiz.altura}")
    else:
        print("El árbol está vacío.")


if __name__ == "__main__":
    main()
