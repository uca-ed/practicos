#include <stdio.h>
#include <stdlib.h>


typedef struct celda {
    int valor;
    struct celda *sig;
} celda_t;


celda_t *CrearCelda(int x) {
    celda_t *nueva = malloc(sizeof(celda_t));
    if (nueva == NULL) {
        fprintf(stderr, "ERROR: sin memoria disponible\n");
        exit(EXIT_FAILURE);
    }
    nueva->valor = x;
    nueva->sig = NULL;
    return nueva;
}


void InsertarPrimero(celda_t **lista, int x) {
    celda_t *nueva = CrearCelda(x);
    nueva->sig = *lista;
    *lista = nueva;
}


int EliminarPrimero(celda_t **lista) {
    if (*lista == NULL) {
        fprintf(stderr, "ERROR: la lista esta vacia\n");
        exit(EXIT_FAILURE);
    }

    celda_t *aux = *lista;
    int valor = aux->valor;
    *lista = aux->sig;
    free(aux);

    return valor;
}


void InsertarFinal(celda_t **lista, int x) {
    celda_t *nueva = CrearCelda(x);

    if (*lista == NULL) {
        *lista = nueva;
        return;
    }

    celda_t *aux = *lista;
    while (aux->sig != NULL) {
        aux = aux->sig;
    }
    aux->sig = nueva;
}


int EliminarUltimo(celda_t **lista) {
    if (*lista == NULL) {
        fprintf(stderr, "ERROR: la lista esta vacia\n");
        exit(EXIT_FAILURE);
    }

    if ((*lista)->sig == NULL) {
        int valor = (*lista)->valor;
        free(*lista);
        *lista = NULL;
        return valor;
    }

    celda_t *aux = *lista;
    while (aux->sig->sig != NULL) {
        aux = aux->sig;
    }

    int valor = aux->sig->valor;
    free(aux->sig);
    aux->sig = NULL;

    return valor;
}

void InsertarPos(celda_t **lista, int x, int pos) {
    if (pos == 0) {
        InsertarPrimero(lista, x);
        return;
    }

    celda_t *aux = *lista;
    int i = 0;
    while (i < pos - 1 && aux != NULL) {
        aux = aux->sig;
        i++;
    }

    if (aux == NULL) {
        fprintf(stderr, "ERROR: posicion invalida\n");
        exit(EXIT_FAILURE);
    }

    celda_t *nueva = CrearCelda(x);
    nueva->sig = aux->sig;
    aux->sig = nueva;
}

int EliminarPos(celda_t **lista, int pos) {
    if (*lista == NULL) {
        fprintf(stderr, "ERROR: la lista esta vacia\n");
        exit(EXIT_FAILURE);
    }

    if (pos == 0) {
        return EliminarPrimero(lista);
    }

    celda_t *aux = *lista;
    int i = 0;
    while (i < pos - 1 && aux->sig != NULL) {
        aux = aux->sig;
        i++;
    }

    if (aux->sig == NULL) {
        fprintf(stderr, "ERROR: posicion invalida\n");
        exit(EXIT_FAILURE);
    }

    celda_t *borrar = aux->sig;
    int valor = borrar->valor;
    aux->sig = borrar->sig;
    free(borrar);

    return valor;
}

int Acceder(celda_t *lista, int pos) {
    celda_t *aux = lista;
    int i = 0;

    while (i < pos && aux != NULL) {
        aux = aux->sig;
        i++;
    }

    if (aux == NULL) {
        fprintf(stderr, "ERROR: posicion invalida\n");
        exit(EXIT_FAILURE);
    }

    return aux->valor;
}

int Longitud(celda_t *lista) {
    int n = 0;
    while (lista != NULL) {
        n++;
        lista = lista->sig;
    }
    return n;
}


void Liberar(celda_t **lista) {
    while (*lista != NULL) {
        EliminarPrimero(lista);
    }
}


void imprimir(celda_t *lista) {
    printf("[ ");
    while (lista != NULL) {
        printf("%d ", lista->valor);
        lista = lista->sig;
    }
    printf("]\n");
}

int main(void) {
    celda_t *lista = NULL;

    InsertarPrimero(&lista, 1);
    InsertarPrimero(&lista, 2);
    InsertarFinal(&lista, 3);
    InsertarFinal(&lista, 4);
    imprimir(lista);                        
    printf("Longitud: %d\n", Longitud(lista));

    printf("EliminarPrimero -> %d\n", EliminarPrimero(&lista));
    imprimir(lista);                   

    printf("EliminarUltimo -> %d\n", EliminarUltimo(&lista));
    imprimir(lista);                     

    InsertarPos(&lista, 5, 1);
    printf("InsertarPos(x=5, pos=1) ->\n");
    imprimir(lista);                        

    printf("Acceder(pos=1) -> %d (sin sacarlo)\n", Acceder(lista, 1));
    imprimir(lista);                          

    printf("EliminarPos(pos=1) -> %d\n", EliminarPos(&lista, 1));
    imprimir(lista);                   

    Liberar(&lista);
    imprimir(lista);                         

    return 0;
}