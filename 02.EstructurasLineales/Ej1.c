#include <stdio.h>
#include <string.h>

#define MAX 100

int cola[MAX];
int inicio = 0;
int cantidad = 0;

void encolar(int valor) {
    if (cantidad == MAX) {
        printf("cola llena, no se pudo encolar %d\n", valor);
        return;
    }
    int pos = (inicio + cantidad) % MAX;
    cola[pos] = valor;
    cantidad++;
}

int desencolar() {
    if (cantidad == 0) {
        printf("cola vacia, no se pudo desencolar\n");
        return -1;
    }
    int valor = cola[inicio];
    inicio = (inicio + 1) % MAX;
    cantidad--;
    return valor;
}

void mostrar() {
    printf("Cola final: ");
    if (cantidad == 0) {
        printf("(vacia)\n");
        return;
    }
    for (int i = 0; i < cantidad; i++) {
        int pos = (inicio + i) % MAX;
        printf("%d ", cola[pos]);
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

        if (strcmp(op, "ENQUEUE") == 0 && leidos == 2) {
            encolar(valor);
        } else if (strcmp(op, "DEQUEUE") == 0) {
            desencolar();
        }
    }

    fclose(f);
    mostrar();
    return 0;
}
