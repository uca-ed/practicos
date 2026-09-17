#include <stdio.h>

#define N 10

typedef struct {
    int datos[N];
    int top;
} PilaArreglo;

PilaArreglo crearPila() {
    PilaArreglo P;
    P.top = -1;
    return P;
}

void Push(PilaArreglo *P, int valor) {
    if (P->top < N - 1) {
        P->top = P->top + 1;
        P->datos[P->top] = valor;
    } else {
        printf("Error:  (Pila llena)\n");
    }
}

int Pop(PilaArreglo *P) {
    if (P->top > -1) {
        int rta = P->datos[P->top];
        P->top = P->top - 1;
        return rta;
    } else {
        printf("Error:  (Pila vacía)\n");
        return -1;
    }
}

void mostrarPila(PilaArreglo *P) {
    if (P->top == -1) {
        printf("La pila está vacía.\n");
        return;
    }
    printf("Resultado final (Fondo -> Tope): [ ");
    for (int i = 0; i <= P->top; i++) {
        printf("%d ", P->datos[i]);
    }
    printf("]\n");
}

int main() {
    
    PilaArreglo P = crearPila();

    Push(&P, 1);
    Push(&P, 2);
    Push(&P, 3);
    Pop(&P);
    Pop(&P);

    mostrarPila(&P);

    return 0;
}