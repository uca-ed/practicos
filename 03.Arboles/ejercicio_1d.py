import sys


def main():
    with open(sys.argv[2]) as f:
        arbol = [int(x) for x in f.read().split()]
    sys.stdout.write("".join(f"{v}\n" for v in arbol))


if __name__ == "__main__":
    main()
