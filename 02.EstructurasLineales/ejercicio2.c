#include <stdio.h>

#define N 100

struct s_pila_arreglo {
	int datos[N];
	int top;
};
typedef struct s_pila_arreglo t_pila;

void crearPila(t_pila* P) {
	P->top = -1;
}

void push(t_pila* P, int valor) {
	if (P->top < N - 1) {
		P->top = P->top + 1;
		P->datos[P->top] = valor;
	} else {
		printf("Error: pila llena");
	}
}

int pop(t_pila* P) {
	if (P->top > -1) {
		int rta = P->datos[P->top];
		P->top = P->top - 1;
		return rta;
	} else {
		printf("Error: pila vacia");
		return -1;
	}
}

void mostrarPila(t_pila* P) {
	printf("Pila final: [ ");
	for (int i = 0; i <= P->top; i++) {
		printf("%d ", P->datos[i]);
	}
	printf("]\n");
}

int main() {
	t_pila P;
	crearPila(&P);
	
	printf("PUSH, 1\n");
	push(&P, 1);
	
	printf("PUSH, 2\n");
	push(&P, 2);
	
	printf("PUSH, 3\n");
	push(&P, 3);
	
	printf("POP,\n");
	pop(&P);
	
	printf("POP,\n");
	pop(&P);
	
	mostrarPila(&P);
	
	return 0;
}
