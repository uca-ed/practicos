#include <stdio.h>
#include <stdlib.h>

typedef struct Celda {
    int valor;
    struct Celda *siguiente;

} Celda;

Celda* crear_celda(int valor) {
    Celda *nueva = (Celda *)malloc(sizeof(Celda));
    if (nueva == NULL) {
        printf( "Error al asignar memoria para la celda.\n");
        exit(1);
    }
    nueva->valor = valor;
    nueva->siguiente = NULL;
    return nueva;
}


void insertarFinal (Celda **cabeza, int valor){
    Celda *nueva = crear_celda(valor);
    if (*cabeza == NULL){
        *cabeza=nueva;
        return;
    }

    Celda *actual = *cabeza;
    while (actual -> siguiente != NULL){
        actual = actual->siguiente;
    }
    actual -> siguiente = nueva;

}

void mostrarLista(Celda *cabeza){
    if (cabeza == NULL){
        
        printf("La lista está vacía.\n");
        return;
    }

    Celda *actual = cabeza;
    while (actual != NULL){
        printf("%d -> ", actual->valor);
        actual = actual->siguiente;
    }
    printf("NULL\n");
}


void liberarLista(Celda **cabeza){
    Celda *actual =*cabeza;
    while(actual !=NULL){
        Celda *aux = actual;
        actual = actual->siguiente;
        free(aux);
    }
    *cabeza=NULL;
}

int main(){
    Celda *lista=NULL;

    insertarFinal(&lista, 10);
    insertarFinal(&lista, 20);
    insertarFinal(&lista, 30);

    mostrarLista(lista);

    liberarLista(&lista);

    return 0;
}

