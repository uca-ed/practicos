#include <stdio.h>

#define BASE 10

void radixSort(int arreglo[], int N) {
    int maximo = arreglo[0];
    for (int i = 1; i < N; i++) {
        if (arreglo[i] > maximo) {
            maximo = arreglo[i];
        }
    }
    int exp = 1;

    while (exp <= maximo) {
        int Q[BASE][N];
        int frente[BASE] = {0};
        int final[BASE] = {0};

        for (int i = 0; i < N; i++) {
            int digito = (arreglo[i] / exp) % 10;
            Q[digito][final[digito]] = arreglo[i];
            final[digito]++;
        }
        int pos = 0;

        for (int i = 0; i < BASE; i++) {
            while (frente[i] < final[i]) {
                arreglo[pos] = Q[i][frente[i]];
                frente[i]++;
                pos++;
            }
        }

       exp = exp * 10;
    }
}

int main() {
    int arreglo[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int N = 8;
    radixSort(arreglo, N);
    printf("Arreglo ordenado: ");
    for (int i = 0; i < N; i++) {
        printf("%d ", arreglo[i]);
    }
    printf("\n");

    return 0;
}
