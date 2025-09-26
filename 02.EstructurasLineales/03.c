#include <stdio.h>
#include <stdlib.h>

struct nodo{
	int val;
	struct nodo* sig;
};

typedef struct nodo* t_nodo;

t_nodo crearLista(int val){
	t_nodo inicio = (t_nodo) malloc(sizeof(struct nodo));
	inicio->val = val;
	inicio->sig = NULL;
	return inicio;
}

void insertarEnListaUltimo(t_nodo *celda,int valor){
	if((*celda)==NULL){
		(*celda) = (t_nodo) malloc(sizeof(struct nodo));
		(*celda)->val = valor;
		(*celda)->sig = NULL;
	}else{
		insertarEnListaUltimo(&((*celda)->sig),valor);
	}
}
	
void insertarEnListaPrimero(t_nodo *celda,int valor){
	if((*celda) == NULL){
		printf("No existe Lista, cree una");
	} else {
		t_nodo aux = (t_nodo) malloc(sizeof(struct nodo));
		aux->val = valor;
		aux->sig = (*celda);
		(*celda) = aux;
	}
}

void insertarEnListaPorPosicion(t_nodo *celda, int valor, int pos){
	if((*celda) != NULL){
		for(int i=0;i<pos-1;i++){
			celda = &((*celda)->sig);
		}
		if((*celda)==NULL){
			printf("ERROR: fuera de index\n");
		} else {
			t_nodo aux = (t_nodo) malloc(sizeof(struct nodo));
			aux->val = valor;
			aux->sig = (*celda);
			(*celda) = aux;
		}
	}
}

int eliminarEnListaUltimo(t_nodo *celda){
	int val;
	if(((*celda)->sig)==NULL){
		val = (*celda)->val;
		free((*celda));
		(*celda) = NULL;
	}else{
		val = eliminarEnListaUltimo(&((*celda)->sig));
	}
	return val;
}
	
int eliminarEnListaPrimero(t_nodo *celda){
	int val;
	t_nodo aux = NULL;
	if((*celda)!=NULL){
		aux = (*celda);
		val = aux->val;
		(*celda) = (*celda)->sig;
		free(aux);
	}
	return val;
}
	
void eliminarEnListaPorValor(t_nodo *c,int sinf, int ssup){
	t_nodo aux = NULL;
	if((*c)!=NULL){
		while((*c)!=NULL){
			if((*c)->val >= sinf && (*c)->val <= ssup){
				aux = (*c);
				(*c) = (*c)->sig;
				free(aux);
			} else {
				c = &((*c)->sig);
			}
		}
	}
}
	
void imprimirLista(t_nodo lista){
	int i = 1;
	while(lista != NULL){
		printf("Elemento %d : %d\n", i, lista->val);
		i++;
		lista = lista->sig;
	}
	printf("\n");
}
	
int main(){
	t_nodo lista = crearLista(8);
	insertarEnListaUltimo(&lista,7);
	insertarEnListaUltimo(&lista,1);
	insertarEnListaUltimo(&lista,15);
	imprimirLista(lista);
	eliminarEnListaPorValor(&lista,6,9);
	insertarEnListaPrimero(&lista,4);
	insertarEnListaPorPosicion(&lista,11,3);
	imprimirLista(lista);
	eliminarEnListaUltimo(&lista);
	imprimirLista(lista);
	return 0;
}

