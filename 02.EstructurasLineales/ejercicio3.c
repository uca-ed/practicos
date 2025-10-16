#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo{
	int dato;
	struct Nodo* siguiente;
}Nodo;


Nodo* crearNodo(int valor) {
	Nodo* nuevoNodo = (Nodo*) malloc(sizeof(Nodo)); // reservar memoria
	if (nuevoNodo != NULL) {
		nuevoNodo->dato = valor;
		nuevoNodo->siguiente = NULL;
	}
	return nuevoNodo;
}


void insertarInicio(Nodo **principio, int valor) {
	Nodo* nuevo = crearNodo(valor);
	if (nuevo != NULL) {
		nuevo->siguiente = *principio; // apunta al primer nodo actual
		*principio = nuevo;             // principio ahora es el nuevo nodo
	}
}



void imprimirLista(Nodo *principio) {
	Nodo *actual = principio;
	while (actual != NULL) {
		printf("%d -> ", actual->dato);
		actual = actual->siguiente;
	}
	printf("NULL\n");
}

