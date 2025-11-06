#include <stdio.h>
#include <stdlib.h>

typedef struct Nodo {
    int valor;
    struct Nodo* izquierdo;
    struct Nodo* derecho;
    int altura;
} Nodo;

int obtenerAltura(Nodo* nodo) {
    if (nodo == NULL)
        return 0;
    return nodo->altura;
}

int maximo(int a, int b) {
    return (a > b) ? a : b;
}

Nodo* crearNodo(int valor) {
    Nodo* nuevo = (Nodo*)malloc(sizeof(Nodo));
    nuevo->valor = valor;
    nuevo->izquierdo = NULL;
    nuevo->derecho = NULL;
    nuevo->altura = 1;
    return nuevo;
}

int obtenerBalance(Nodo* nodo) {
    if (nodo == NULL)
        return 0;
    return obtenerAltura(nodo->izquierdo) - obtenerAltura(nodo->derecho);
}

Nodo* rotarDerecha(Nodo* y) {
    Nodo* x = y->izquierdo;
    Nodo* T2 = x->derecho;
    x->derecho = y;
    y->izquierdo = T2;
    y->altura = maximo(obtenerAltura(y->izquierdo), obtenerAltura(y->derecho)) + 1;
    x->altura = maximo(obtenerAltura(x->izquierdo), obtenerAltura(x->derecho)) + 1;
    return x;
}

Nodo* rotarIzquierda(Nodo* x) {
    Nodo* y = x->derecho;
    Nodo* T2 = y->izquierdo;
    y->izquierdo = x;
    x->derecho = T2;
    x->altura = maximo(obtenerAltura(x->izquierdo), obtenerAltura(x->derecho)) + 1;
    y->altura = maximo(obtenerAltura(y->izquierdo), obtenerAltura(y->derecho)) + 1;
    return y;
}

Nodo* insertar(Nodo* nodo, int valor) {
    if (nodo == NULL)
        return crearNodo(valor);
    if (valor < nodo->valor)
        nodo->izquierdo = insertar(nodo->izquierdo, valor);
    else if (valor > nodo->valor)
        nodo->derecho = insertar(nodo->derecho, valor);
    else
        return nodo;

    nodo->altura = 1 + maximo(obtenerAltura(nodo->izquierdo), obtenerAltura(nodo->derecho));
    int balance = obtenerBalance(nodo);

    if (balance > 1 && valor < nodo->izquierdo->valor)
        return rotarDerecha(nodo);
    if (balance < -1 && valor > nodo->derecho->valor)
        return rotarIzquierda(nodo);
    if (balance > 1 && valor > nodo->izquierdo->valor) {
        nodo->izquierdo = rotarIzquierda(nodo->izquierdo);
        return rotarDerecha(nodo);
    }
    if (balance < -1 && valor < nodo->derecho->valor) {
        nodo->derecho = rotarDerecha(nodo->derecho);
        return rotarIzquierda(nodo);
    }

    return nodo;
}

void recorridoEnOrden(Nodo* nodo) {
    if (nodo != NULL) {
        recorridoEnOrden(nodo->izquierdo);
        printf("%d ", nodo->valor);
        recorridoEnOrden(nodo->derecho);
    }
}

int main() {
    Nodo* raiz = NULL;
    int valores[] = {10, 20, 30, 40, 50, 25};  //tomo estos valores, podriamos sacarlos de un archivo, pero tendria que leer el archivo (faltaria el codigo)
    int n = sizeof(valores) / sizeof(valores[0]);

    for (int i = 0; i < n; i++) {
        raiz = insertar(raiz, valores[i]);
    }

    printf("Recorrido en orden del árbol AVL:\n");
    recorridoEnOrden(raiz);
    printf("\n");

    return 0;
}
