#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void preorden(char arbol[], int i, int n, int grado) {
    if (i >= n) return;
    printf("%c ", arbol[i]);
    for (int j = 1; j <= grado; j++) {
        int hijo = grado * i + j;
        if (hijo < n)
            preorden(arbol, hijo, n, grado);
    }
}

int main() {
    FILE *fgrado, *fnodos;
    int grado;
    char arbol[100];
    int n = 0;
    fgrado = fopen("grado.txt", "r");
    if (fgrado == NULL) {
        printf("Error al abrir grado.txt\n");
        return 1;
    }
    fscanf(fgrado, "%d", &grado);
    fclose(fgrado);
    fnodos = fopen("nodos.txt", "r");
    if (fnodos == NULL) {
        printf("Error al abrir nodos.txt\n");
        return 1;
    }
    while (fscanf(fnodos, " %c", &arbol[n]) == 1) {
        n++;
    }
    fclose(fnodos);
    printf("Grado del árbol: %d\n", grado);
    printf("Número de nodos: %d\n", n);
    double hreal = log(((n - 1) * (grado - 1) + 1)) / log(grado); // calcular altura sin recorrer
    int altura = (int)ceil(hreal);
    printf("Altura del árbol (sin recorrido): %d\n", altura);
    printf("Recorrido preorden: ");
    preorden(arbol, 0, n, grado);
    printf("\n");
    return 0;
}
