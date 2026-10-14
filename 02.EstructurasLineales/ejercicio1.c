#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

struct s_cola_arreglo {
    int datos[MAX];
    int inicio;
    int longitud;
};
typedef struct s_cola_arreglo t_cola;

void crearCola(t_cola* cola) {
    cola->inicio = 0;
    cola->longitud = 0;
}

void encolar(t_cola* cola, int valor) {
    if (cola->longitud < MAX) {
        int pos = (cola->inicio + cola->longitud) % MAX;
        cola->datos[pos] = valor;
        cola->longitud = cola->longitud + 1;
    } else {
        printf("Error: Cola llena\n");
    }
}

int desencolar(t_cola* cola) {
    if (cola->longitud > 0) {
        int valor = cola->datos[cola->inicio];
        cola->inicio = (cola->inicio + 1) % MAX;
        cola->longitud = cola->longitud - 1;
        return valor;
    } else {
        printf("Error: Cola vacia\n");
        return -1;
    }
}

void mostrarCola(t_cola* cola) {
    printf("Resultado final de la cola: [ ");
    for (int i = 0; i < cola->longitud; i++) {
        int pos = (cola->inicio + i) % MAX;
        printf("%d ", cola->datos[pos]);
    }
    printf("]\n");
}

int main() {
	t_cola cola;
	crearCola(&cola);
	
	printf("ENQUEUE, 1\n");
	encolar(&cola, 1);
	
	printf("ENQUEUE, 2\n");
	encolar(&cola, 2);
	
	printf("ENQUEUE, 3\n");
	encolar(&cola, 3);
	
	printf("ENQUEUE, 4\n");
	encolar(&cola, 4);
	
	printf("DEQUEUE,\n");
	desencolar(&cola);
	
	printf("DEQUEUE,\n");
	desencolar(&cola);
	
	mostrarCola(&cola);
	
	return 0;
}
