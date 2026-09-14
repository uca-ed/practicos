#include <stdio.h>
#include <stdlib.h>

struct s_lista{
    int valor;
    struct s_lista* sig;
};

typedef struct s_lista t_l;

void crear_lista(t_l** l){
    *l = NULL;
}

int agregar_elemento(t_l** l, int valor, int N){

    t_l* nuevo = malloc(sizeof(t_l));

    nuevo->valor = valor;
    nuevo->sig = NULL;

    if (*l == NULL){
        *l = nuevo;
    }
    else{
        t_l* nodo = *l;

        while (nodo->sig != NULL){
            nodo = nodo->sig;
        }

        nodo->sig = nuevo;
    }

    N++;

    return N;
}

int eliminar_elemento(t_l** l, int valor){

    int valor_eliminado = 0;
    t_l* nodo = *l;
    t_l* anterior = NULL;

    while (nodo != NULL && nodo->valor != valor){
        anterior = nodo;
        nodo = nodo->sig;
    }

    if (nodo != NULL){
        valor_eliminado = nodo->valor;
        if (anterior == NULL){
            *l = nodo->sig;
        }
        else{
            anterior->sig = nodo->sig;
        }
        free(nodo);
    }

    return valor_eliminado;
}

void mostrar_lista(t_l* l){
    t_l* nodo = l;
    while (nodo != NULL){
        printf("%d -> ", nodo->valor);
        nodo = nodo->sig;
    }
    printf("NULL\n");
}
int main(){

    t_l* lista;
    int N = 0;
    int eliminado;
    crear_lista(&lista);

    N = agregar_elemento(&lista, 10, N);
    N = agregar_elemento(&lista, 20, N);
    N = agregar_elemento(&lista, 30, N);
    N = agregar_elemento(&lista, 40, N);

    printf("Lista:\n");
    mostrar_lista(lista);

    printf("Cantidad de elementos: %d\n", N);

    eliminado = eliminar_elemento(&lista, 20);

    printf("\nElemento eliminado: %d\n", eliminado);

    printf("Lista despues de eliminar:\n");
    mostrar_lista(lista);

    return 0;
}
