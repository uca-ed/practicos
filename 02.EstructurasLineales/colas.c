#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct colas{
    int* cola;
    int largo;
    int elementos;
    int inicio;
};



struct colas crearCola(int largo){
    struct colas cola;
    //int arr[largo];
    cola.largo=largo;
    cola.cola = malloc(largo);
    cola.elementos=0;
    cola.inicio=0;
    return cola;
}

void enqueue(struct colas *cola,int valor){
    if(cola->elementos < cola->largo){
        cola->cola[(cola->inicio+cola->elementos)%cola->largo] = valor;
        printf("Inicio: %i || elementos:%i || largo: %i\n",cola->inicio,cola->elementos,cola->largo);
        printf("incerte en la cola, pos: %i el valor : %i\n",(cola->inicio+cola->elementos)%cola->largo,valor);
        cola->elementos+=1;
    }else{
        printf("cola llena");
    }
}

int dequeue(struct colas *cola){
    int valor=0;
    if(cola->elementos!=0){
        valor=cola->cola[cola->inicio];
        cola->inicio = (cola->inicio+1)%cola->largo;
        cola->elementos--;
    }
    return valor;
}


int main() {
    struct colas cola = crearCola(5);
    FILE *archivo = fopen("datos.csv", "r");
    char buffer[256];

    if (archivo == NULL) {
        perror("Error al abrir");
        return EXIT_FAILURE;
    }

    // 1. Leemos la línea completa primero
    while (fgets(buffer, sizeof(buffer), archivo) != NULL) {
        printf("Leido: %s\n", buffer);

        char *fragmento = strtok(buffer, ",");
        printf("Fragmento : %s\n",fragmento);
        if(strcmp(fragmento,"ENQUEUE")==0){
            printf("Numero a agregar : %i \n", (int) (buffer[8] - '0'));
            enqueue(&cola,(int)(buffer[8] - '0'));
        }
        else if(strcmp(fragmento,"DEQUEUE")==0){
            printf("Elimine : %i\n",dequeue(&cola));
        }

    }

    fclose(archivo);
    printf("ARREGLO FINAL:  ");
    for(int i=0;i<cola.largo;i++){
        printf("[%i]",cola.cola[i]);
    }
    return EXIT_SUCCESS;
}