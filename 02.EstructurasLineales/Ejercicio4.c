#include <stdio.h>
#include <string.h>

#define MAX_PALABRAS 1000
#define MAX_LONG 100

typedef struct {
	char datos[MAX_PALABRAS][MAX_LONG];
	int frente;
	int fin;
} Cola;

static char palabras[MAX_PALABRAS][MAX_LONG];
static Cola baldes[27]; // 27 colas --> para todas las letras del abecedario

void enqueue(Cola *c, char palabra[]) {
	strcpy(c -> datos[c->fin], palabra);
	c -> fin++;
}

int dequeue(Cola *c, char destino[]) {
	if (c -> frente == c -> fin) return 0; // cola vacía
	strcpy(destino, c -> datos[c -> frente]);
	c->frente++;
	return 1;
}

int leer_archivo(char nombre[], int *max_len) {
	FILE *f = fopen(nombre, "r");
	int cant_palabras = 0;
	
	while (fgets(palabras[cant_palabras], MAX_LONG, f) != NULL) {
		palabras[cant_palabras][strcspn(palabras[cant_palabras], "\r\n")] = '\0';
		if ((int)strlen(palabras[cant_palabras]) > *max_len) {
			*max_len = strlen(palabras[cant_palabras]);
		}
		cant_palabras++;
	}
	
	fclose(f);
	return cant_palabras;
}

void radix_sort(int cant_palabras, int max_len) {
	// Recorre las posiciones desde la última letra hasta la primera
	for (int pos = max_len - 1; pos >= 0; pos--) {
		
		// Vacía y prepara las 27 colas
		for (int b = 0; b < 27; b++) {
			baldes[b].frente = 0;
			baldes[b].fin = 0;
		}
		
		// Cada palabra se encola en la cola que le corresponde según la letra que tiene en 'pos'
		for (int i = 0; i < cant_palabras; i++) {
			int indice;
			if (pos < (int)strlen(palabras[i])) {
				indice = palabras[i][pos] - 'a' + 1;
			} else {
				indice = 0;
			}
			enqueue(&baldes[indice], palabras[i]);
		}
		
		// Se desencolan las 27 colas en orden y se vuelve a armar 'palabras' ordenado
		int k = 0;
		char palabra[MAX_LONG];
		for (int b = 0; b < 27; b++) {
			while (dequeue(&baldes[b], palabra)) {
				strcpy(palabras[k], palabra);
				k++;
			}
		}
	}
}

int main() {
	char nombre_archivo[MAX_LONG];
	int max_len = 0;
	
	printf("Nombre del archivo a ordenar: ");
	scanf("%s", nombre_archivo);
	
	int cant_palabras = leer_archivo(nombre_archivo, &max_len);
	
	printf("\nArchivo desordenado:\n");
	for (int i = 0; i < cant_palabras; i++) {
		printf("%s\n", palabras[i]);
	}

	radix_sort(cant_palabras, max_len);
	
	printf("\nResultado ordenado:\n");
	for (int i = 0; i < cant_palabras; i++) {
		printf("%s\n", palabras[i]);
	}
	
	return 0;
}
