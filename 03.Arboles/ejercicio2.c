#include <stdio.h>
#include <stdlib.h>
typedef struct nodo{
    int clave;
    struct nodo* izquierda;
    struct nodo* derecha;
    int altura;
}nodo;

int altura(nodo* N){
    if(N==NULL){
        return 0;
    }
    return N->altura;
}

int max(int a, int b) {
    if (a > b){
        return a;
    }
    else{
        return b;
    }
}

nodo* crearNodo(int clave) {
    nodo* n = (nodo*)malloc(sizeof(nodo));
    if (!n) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    n->clave = clave;
    n->izquierda = NULL;
    n->derecha = NULL;
    n->altura = 1;
    return n;
}

//caso 1: rotacion simple a la derecha (RR)
nodo* rotarDerecha(nodo* y){
    nodo* x= y -> izquierda;
    nodo* T2= x->derecha;
    x->derecha=y;
    y->izquierda=T2;
    y->altura=1+max(altura(y->izquierda),altura(y->derecha));
    x->altura=1+max(altura(x->izquierda),altura(x->derecha));
    return x;
}
//caso2: rotacion simple a la izquierda (LL)
nodo* rotarIzquierda(nodo* x){
    nodo* y= x -> derecha;
    nodo* T2=y->izquierda;
    y->izquierda=x;
    x->derecha=T2;
    x->altura=1+max(altura(x->izquierda),altura(x->derecha));
    y->altura=1+max(altura(y->izquierda),altura(y->derecha));
    return y;
}
//caso 3: rotaciones dobles
//rotacion izquierda-derecha (LR)
nodo* rotarIzquierdaDerecha(nodo* z) {
    // 'z' es el nodo desbalanceado
    // 'y' es su hijo izquierdo
    nodo* y = z->izquierda;
    z->izquierda = rotarIzquierda(y); //rotamos a la izquierda sobre y
    return rotarDerecha(z);// rotamos a la derecha sobre z
}
//rotacion derecha-izquierda (RL)
nodo* rotarDerechaIzquierda(nodo* z) {
    nodo* y = z->derecha;
    z->derecha = rotarDerecha(y); //rotamos a la derecha sobre y
    return rotarIzquierda(z); //rotamos a la izquierda sobre z
}

//codigo para comrobar el balance y rotar si hace falta
int getBalance(nodo* N) {
    if (N == NULL) return 0;
    return altura(N->izquierda) - altura(N->derecha);
}
nodo* insertarNodo(nodo* nodo, int clave) {
    if (nodo == NULL)
        return crearNodo(clave);
    if (clave < nodo->clave)
        nodo->izquierda = insertarNodo(nodo->izquierda, clave);
    else if (clave > nodo->clave)
        nodo->derecha = insertarNodo(nodo->derecha, clave);
    else
        return nodo;
    nodo->altura = 1 + max(altura(nodo->izquierda), altura(nodo->derecha)); //actualizar altuda
    int balance = getBalance(nodo);
    if (balance > 1 && clave < nodo->izquierda->clave) //LL
        return rotarDerecha(nodo);
    if (balance < -1 && clave > nodo->derecha->clave) //RR
        return rotarIzquierda(nodo);
    if (balance > 1 && clave > nodo->izquierda->clave) { //LR
        nodo->izquierda = rotarIzquierda(nodo->izquierda);
        return rotarDerecha(nodo);
    }
    if (balance < -1 && clave < nodo->derecha->clave) { //RL
        nodo->derecha = rotarDerecha(nodo->derecha);
        return rotarIzquierda(nodo);
    }
    return nodo;
}
void preOrden(nodo* root) {
    if (root != NULL) {
        printf("%d ", root->clave);
        preOrden(root->izquierda);
        preOrden(root->derecha);
    }
}
void inOrden(nodo* root) {
    if (root != NULL) {
        inOrden(root->izquierda);
        printf("%d ", root->clave);
        inOrden(root->derecha);
    }
}
int main() {
    FILE* archivo;
    archivo = fopen("datos.txt", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo de datos.\n");
        return 1;
    }
    nodo* raiz = NULL;
    int clave;
    printf("Insertando claves desde el archivo:\n");
    while (fscanf(archivo, "%d", &clave) == 1) {
        printf("Insertando %d...\n", clave);
        raiz = insertarNodo(raiz, clave);
    }
    fclose(archivo);
    printf("\nRecorrido INORDEN (ordenado): ");
    inOrden(raiz);
    printf("\nRecorrido PREORDEN (estructura AVL): ");
    preOrden(raiz);
    printf("\n");
    return 0;
}