```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Celda {
    int valor;
    struct Celda *siguiente;
} Celda;

int main() {

    Celda *primera = NULL;

    Celda *celda1 = malloc(sizeof(Celda));
    Celda *celda2 = malloc(sizeof(Celda));
    Celda *celda3 = malloc(sizeof(Celda));

    celda1->valor = 10;
    celda2->valor = 20;
    celda3->valor = 30;

    celda1->siguiente = celda2;
    celda2->siguiente = celda3;
    celda3->siguiente = NULL;

    primera = celda1;

    Celda *actual = primera;

    while (actual != NULL) {
        printf("%d ", actual->valor);
        actual = actual->siguiente;
    }

    printf("\n");

    free(celda1);
    free(celda2);
    free(celda3);

    return 0;
}
```
