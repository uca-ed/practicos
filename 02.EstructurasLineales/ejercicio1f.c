#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 7 //defino en 7 el tamaño

//Nodo de la cola "elemento"
typedef struct{
	int array[MAX];
	int principio; //indice 1er elemento
	int final; //indice último elemento
}Cola;

void constructor(Cola *q){
	q->principio = -1;
	q->final = -1;
}
	
void enqueue(Cola *q, int elemento){
	if (q->final == MAX - 1){
		printf("ERROR. La cola está llena.");
		return;
	}
	else if((q->principio == -1) && (q->final == -1)){
		//mi cola esta vacia
		(q->principio) = (q->principio) + 1;
		(q->final) =  (q->final) + 1;
	}
	else{
		(q->final) = (q->final) + 1;
	}
	(q->array)[q->final] = elemento;	
}
	
	
int dequeue(Cola *q){
	int res;
	if( ((q->principio) == -1) && ((q->final) == -1)){
		printf("ERROR. La cola está vacia");
		return -1;
	}
	else{
		res = (q->array)[q->final];
		if ((q->principio) == (q->final)){
			q->principio = -1;
			q->final = -1;
		}
		else{
			q->principio = (q->principio) + 1;
		}	
	}
	return res;
}
	
void mostrarCola(Cola *q){
	if (q->principio == -1) {
		printf("La cola está vacía.\n");
		return;
	}
	
	printf("La cola es: \n");
	for (int i = q->principio; i <= q->final; i++) {
		printf("%d\n", q->array[i]);
	}
}	
	
	


int main(int argc, char *argv[]) {
	Cola q;
	constructor(&q);
	
	FILE *archivo = fopen("ejercicio1.txt", "r"); //abro archivo
	if(!archivo){
		printf("Hubo un error al abrir el archivo.\n");
		return -1;
	}
	
	char linea[50];
	while(fgets(linea, sizeof(linea), archivo)){
		if(strncmp(linea, "enqueue", 7) == 0){
			int valor;
			sscanf(linea, "enqueue(%d)", &valor); //agarro el numero
			enqueue(&q, valor); //lo meto a la cola
		}
		else if(strncmp(linea, "dequeue", 7) == 0){
			dequeue(&q); //saco el valor de la cola
		}
	}
	
	fclose(archivo); //cierro archivo
	mostrarCola(&q); //veo pila
	return 0;
	
}

