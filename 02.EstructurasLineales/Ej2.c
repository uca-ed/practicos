#include <stdio.h>
#include <string.h>

#define MAX 100

int pila[MAX];
int tope = -1;

void apilar(int valor) {
    if (tope == MAX - 1) {
        printf("pila llena, no se pudo apilar %d\n", valor);
        return;
    }
    tope++;
    pila[tope] = valor;
}

int desapilar() {
    if (tope == -1) {
        printf("pila vacia, no se pudo desapilar\n");
        return -1;
    }
    int valor = pila[tope];
    tope--;
    return valor;
}

void mostrar() {
    printf("Pila final (de abajo a arriba): ");
    if (tope == -1) {
        printf("(vacia)\n");
        return;
    }
    for (int i = 0; i <= tope; i++) {
        printf("%d ", pila[i]);
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("uso: %s archivo.txt\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        printf("no se pudo abrir %s\n", argv[1]);
        return 1;
    }

    char linea[100];
    while (fgets(linea, sizeof(linea), f) != NULL) {
        linea[strcspn(linea, "\n")] = '\0';
        if (strlen(linea) == 0) continue;

        char op[20];
        int valor;
        int leidos = sscanf(linea, "%19[^,],%d", op, &valor);

        if (strcmp(op, "PUSH") == 0 && leidos == 2) {
            apilar(valor);
        } else if (strcmp(op, "POP") == 0) {
            desapilar();
        }
    }

    fclose(f);
    mostrar();
    return 0;
}
