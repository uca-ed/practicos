#include <stdio.h>
#include <string.h>
#define MAX 7

typedef struct{
	int arreglo[MAX];
	int tope;
}Pila;

void constructor(Pila *p){
	p->tope = -1;
}
	
	
void push(Pila *p, int elem){
	if((p->tope) == MAX-1){
		printf("ERROR. La pila está llena");
		return;
	}
	else{
		p->tope = (p->tope) + 1;
		(p->arreglo)[p->tope] = elem;
	}
}
	
int pop(Pila *p){
	
	if( (p->tope) == -1){
		printf("ERROR. La pila esta vacia");
		return -1;//error
	}
	else{
		int elemento = (p->arreglo)[p->tope];
		p->tope = (p->tope) - 1;
		return elemento;
	}
}
	
	
	
void mostrarPila(Pila *p){
	if(p->tope == -1){
		printf("La pila esta vacia\n");
		return;
	}
	printf("La pila es: \n");
	for(int i = p->tope; i>=0;i--){
		printf("%d\n", (p->arreglo)[i]);
	}
}
	
int main(){
	Pila p;
	constructor(&p);
		
	FILE *archivo = fopen("ejercicio2.txt", "r"); //abro archivo
	if(!archivo){
		printf("Hubo un error al abrir el archivo.\n");
		return -1;
	}
		
	char linea[50];
	while(fgets(linea, sizeof(linea), archivo)){
		if(strncmp(linea, "push", 4) == 0){
			int valor;
			sscanf(linea, "push(%d)", &valor); //agarro el numero
			push(&p, valor); //lo meto a la pila
		}
		else if(strncmp(linea, "pop", 3) == 0){
			pop(&p); //saco el valor de la pila
		}
	}
		
	fclose(archivo); //cierro archivo
	mostrarPila(&p); //veo pila
	return 0;
	}
