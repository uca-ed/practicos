#include <stdio.h>
#include <stdlib.h>

struct s_nodo {
	int valor;
	struct s_nodo* sig;
};
typedef struct s_nodo* t_nodo;

void insertarPrimero(t_nodo* nodo, int valor){
	t_nodo aux = malloc(sizeof(struct s_nodo));
	aux->valor = valor;
	aux->sig = *nodo;
	*nodo = aux;
}

void eliminar(t_nodo* nodo, int valor){ //Esta funcion eliminar por valor
	t_nodo aux;
	
	while (*nodo != NULL && (*nodo)->valor != valor){
		nodo = &(*nodo)->sig;
	}
	if (*nodo != NULL){
		aux = *nodo;
		*nodo = (*nodo)->sig;
		free(aux);
	}
}

void append(t_nodo* nodo, int valor){ //esta funcion agrega elementos al final de la lista
	t_nodo aux;
	aux = malloc(sizeof(struct s_nodo));
	aux->valor = valor;
	aux->sig = NULL;
	
	if (*nodo == NULL){
		*nodo = aux;
	}
	else {
		while ((*nodo)->sig != NULL) {
			nodo = &(*nodo)->sig;
		}
		(*nodo)->sig = aux;
	}
}

void mostrar(t_nodo nodo){
	while (nodo != NULL){
		printf("%d ", nodo->valor);
		nodo = nodo->sig;
	}
}

int main() {
	t_nodo lista = NULL;
	insertarPrimero(&lista, 10);
	insertarPrimero(&lista, 20);
	append(&lista, 30);
	append(&lista, 40);
	
	printf("Lista: ");
	
	mostrar(lista);
	eliminar(&lista, 20);
	
	printf("\nLista despues de eliminar: ");
	mostrar(lista);
	
	return 0;
}
