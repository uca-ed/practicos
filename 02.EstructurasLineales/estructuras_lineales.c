// operaciones.txt
/*
encolar 1
encolar 2 
desencolar 
encolar 3
desencolar
*/

// EJERCICIO 1
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    int datos[MAX];
    int frente;
    int final;
    int tamaño;
} Cola;

void inicializar(Cola *q) {
    q->frente = 0;
    q->final = -1;
    q->tamaño = 0;
}

void encolar(Cola *q, int valor) {
    if (q->tamaño == MAX) {
        printf("Cola llena\n");
        return;
    }
    q->final = (q->final + 1) % MAX;
    q->datos[q->final] = valor;
    q->tamaño++;
}

int desencolar(Cola *q) {
    if (q->tamaño == 0) {
        printf("Cola vacía\n");
        return -1;
    }
    int valor = q->datos[q->frente];
    q->frente = (q->frente + 1) % MAX;
    q->tamaño--;
    return valor;
}

void mostrar(Cola q) {
    printf("Cola: ");
    for (int i = 0; i < q.tamaño; i++) {
        int pos = (q.frente + i) % MAX;
        printf("%d ", q.datos[pos]);
    }
    printf("\n");
}

void procesarArchivo(const char* nombre_archivo) {
    FILE *archivo = fopen(nombre_archivo, "r");
    if (!archivo) {
        perror("Error al abrir archivo");
        return;
    }

    Cola q;
    inicializar(&q);
    char linea[50];
    char operacion[10];
    int valor;
    // esto lo hago cuando tengo string y un numero entero en el archivo de texto
    while (fgets(linea, sizeof(linea), archivo)) {
        if (sscanf(linea, "%s %d", operacion, &valor) == 2) {
            if (strcmp(operacion, "encolar") == 0) {
                encolar(&q, valor);
            } else if (strcmp(operacion, "desencolar") == 0) {
                desencolar(&q);
            }
        } else if (sscanf(linea, "%s", operacion) == 1) {
            if (strcmp(operacion, "desencolar") == 0) {
                desencolar(&q);
            }
        }
    }

    mostrar(q);
    fclose(archivo);
}

int main() {
    procesarArchivo("operaciones.txt");
    return 0;
}


// operaciones_pila.txt
/*
apilar 10
apilar 20
apilar 30
desapilar
apilar 40
apilar 50
desapilar
desapilar
apilar 60
apilar 70
*/
// EJERCICIO 2
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

typedef struct {
    int data[MAX_SIZE];
    int top;
} Pila;

void inicializar(Pila *p) {
    p->top = -1;
}

void apilar(Pila *p, int valor) {
    if (p->top == MAX_SIZE - 1) {
        printf("Error: Pila llena\n");
        return;
    }
    p->data[++p->top] = valor;
}

int desapilar(Pila *p) {
    if (p->top == -1) {
        printf("Error: Pila vacía\n");
        return -1;
    }
    return p->data[p->top--];
}

void mostrar(Pila p) {
    printf("Estado final de la pila: [");
    for (int i = 0; i <= p.top; i++) {
        printf("%d", p.data[i]);
        if (i < p.top) printf(", ");
    }
    printf("]\n");
}

void procesarArchivo(const char* filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error al abrir el archivo");
        return;
    }

    Pila p;
    inicializar(&p);
    char line[100];
    char operacion[10];
    int valor;

    while (fgets(line, sizeof(line), file)) {
        if (sscanf(line, "%s %d", operacion, &valor) == 2) {
            if (strcmp(operacion, "apilar") == 0) {
                apilar(&p, valor);
            }
        } else if (sscanf(line, "%s", operacion) == 1) {
            if (strcmp(operacion, "desapilar") == 0) {
                desapilar(&p);
            }
        }
    }

    mostrar(p);
    fclose(file);
}

int main() {
    procesarArchivo("operaciones_pila.txt");
    return 0;
}


// operaciones_lista.txt
/*
insertarInicio 5
insertarFinal 10
insertarFinal 15
eliminar 10
insertarInicio 2
*/

// EJERCICIO 3
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Nodo {
    int dato;
    struct Nodo* siguiente;
} Nodo;

typedef struct {
    Nodo* cabeza;
    int tamaño;
} Lista;
Nodo* crear_nodo(int dato) {
    Nodo* nuevo = (Nodo*)malloc(sizeof(Nodo));
    if (nuevo == NULL) {
        printf("Error al asignar memoria\n");
        exit(1);
    }
    nuevo->dato = dato;
    nuevo->siguiente = NULL;
    return nuevo;
}

void inicializarLista(Lista* lista) {
    lista->cabeza = NULL;
    lista->tamaño = 0;
}
void insertarInicio(Lista* lista, int dato) {
    Nodo* nuevo = crear_nodo(dato);
    nuevo->siguiente = lista->cabeza;
    lista->cabeza = nuevo;
    lista->tamaño++;
}

void insertarFinal(Lista* lista, int dato) {
    Nodo* nuevo = crear_nodo(dato);
    
    if (lista->cabeza == NULL) {
        lista->cabeza = nuevo;
    } else {
        Nodo* actual = lista->cabeza;
        while (actual->siguiente != NULL) {
            actual = actual->siguiente;
        }
        actual->siguiente = nuevo;
    }
    lista->tamaño++;
}
int eliminarNodo(Lista* lista, int dato) {
    Nodo* actual = lista->cabeza;
    Nodo* anterior = NULL;
    
    while (actual != NULL) {
        if (actual->dato == dato) {
            if (anterior == NULL) {
                lista->cabeza = actual->siguiente;
            } else {
                anterior->siguiente = actual->siguiente;
            }
            free(actual);
            lista->tamaño--;
            return 1;
        }
        anterior = actual;
        actual = actual->siguiente;
    }
    return 0;
}
void mostrarLista(Lista lista) {
    Nodo* actual = lista.cabeza;
    printf("Lista [%d elementos]: ", lista.tamaño);
    while (actual != NULL) {
        printf("%d -> ", actual->dato);
        actual = actual->siguiente;
    }
    printf("NULL\n");
}
void liberarLista(Lista* lista) {
    Nodo* actual = lista->cabeza;
    while (actual != NULL) {
        Nodo* temp = actual;
        actual = actual->siguiente;
        free(temp);
    }
    lista->cabeza = NULL;
    lista->tamaño = 0;
}
void procesarArchivo(Lista* lista, const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error al abrir archivo");
        return;
    }

    char operacion[20];
    int valor;

    while (fscanf(file, "%s %d", operacion, &valor) == 2) {
        if (strcmp(operacion, "insertarInicio") == 0) {
            insertarInicio(lista, valor);
        } else if (strcmp(operacion, "insertarFinal") == 0) {
            insertarFinal(lista, valor);
        } else if (strcmp(operacion, "eliminar") == 0) {
            eliminarNodo(lista, valor);
        }
    }

    fclose(file);
}
int main() {
    Lista mi_lista;
    inicializarLista(&mi_lista);

    procesarArchivo(&mi_lista, "operaciones_lista.txt");
    // liberarLista(&mi_lista);
    mostrarLista(mi_lista);
    liberarLista(&mi_lista);

    return 0;
}


// palabras.txt
/*
gonzalo
rogelio
carlos
sofía
pedro
laura
elena
*/

// EJERCICIO 4
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PALABRAS 1000
#define MAX_LARGO 100

void contar_max_largo(char palabras[][MAX_LARGO], int n, int* max_largo) {
    *max_largo = 0;
    for (int i = 0; i < n; i++) {
        int len = strlen(palabras[i]);
        if (len > *max_largo) *max_largo = len;
    }
}
void radix_sort(char palabras[][MAX_LARGO], int n) {
    char salida[MAX_PALABRAS][MAX_LARGO];
    int count[256];
    int max_largo;

    contar_max_largo(palabras, n, &max_largo);

    for (int pos = max_largo - 1; pos >= 0; pos--) {
        memset(count, 0, sizeof(count));

        for (int i = 0; i < n; i++) {
            int c = (pos < strlen(palabras[i])) ? (unsigned char)palabras[i][pos] : 0;
            count[c]++;
        }

        for (int i = 1; i < 256; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int c = (pos < strlen(palabras[i])) ? (unsigned char)palabras[i][pos] : 0;
            strcpy(salida[--count[c]], palabras[i]);
        }

        for (int i = 0; i < n; i++) {
            strcpy(palabras[i], salida[i]);
        }
    }
}
void mostrar_palabras(char palabras[][MAX_LARGO], int n) {
    printf("Palabras ordenadas:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", palabras[i]);
    }
}
int procesarArchivo(char palabras[][MAX_LARGO], const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error al abrir archivo");
        return 0;
    }

    int cantidad = 0;
    while (fscanf(file, "%s", palabras[cantidad]) == 1 && cantidad < MAX_PALABRAS) {
        cantidad++;
    }

    fclose(file);
    return cantidad;
}

int main() {
    char palabras[MAX_PALABRAS][MAX_LARGO];
    int cantidad = procesarArchivo("palabras.txt", palabras);

    radix_sort(palabras, cantidad);

    mostrar_palabras(palabras, cantidad);
    return 0;
}


// grafo.txt

/*

*/
// EJERCICIO 5

#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

typedef struct Nodo {
    int destino;
    struct Nodo* siguiente;
} Nodo;

typedef struct {
    int numVertices;
    Nodo* adyacencia[MAX_VERTICES];
} Grafo;

Nodo* crearNodo(int destino) {
    Nodo* nuevo = malloc(sizeof(Nodo));
    nuevo->destino = destino;
    nuevo->siguiente = NULL;
    return nuevo;
}
void inicializarGrafo(Grafo* grafo, int n) {
    grafo->numVertices = n;
    for (int i = 0; i < n; i++) {
        grafo->adyacencia[i] = NULL;
    }
}


void agregarArista(Grafo* grafo, int origen, int destino) {
    Nodo* nuevo = crearNodo(destino);
    nuevo->siguiente = grafo->adyacencia[origen];
    grafo->adyacencia[origen] = nuevo;
}

int dfs(Grafo* grafo, int v, int* visitado, int* pila, int* tsort, int* idx) {
    visitado[v] = 1;
    pila[v] = 1;

    Nodo* actual = grafo->adyacencia[v];
    while (actual != NULL) {
        int w = actual->destino;
        if (!visitado[w]) {
            if (!dfs(grafo, w, visitado, pila, tsort, idx))
                return 0;
        } else if (pila[w]) {
            return 0;
        }
        actual = actual->siguiente;
    }

    pila[v] = 0;
    tsort[(*idx)--] = v;
    return 1;
}

int tSort(Grafo* grafo, int* tsort) {
    int visitado[MAX_VERTICES] = {0};
    int pila[MAX_VERTICES] = {0};
    int idx = grafo->numVertices - 1;

    for (int i = 0; i < grafo->numVertices; i++) {
        if (!visitado[i]) {
            if (!dfs(grafo, i, visitado, pila, tsort, &idx)) {
                return 0;
            }
        }
    }
    return 1;
}

int main() {
    Grafo grafo;
    inicializarGrafo(&grafo, 6);

    agregarArista(&grafo, 5, 2);
    agregarArista(&grafo, 5, 0);
    // agregarArista(&grafo, 1, 5);
    agregarArista(&grafo, 3, 1);

    int tsort[MAX_VERTICES];
    if (tSort(&grafo, tsort)) {
        printf("Orden topologico:\n");
        for (int i = 0; i < grafo.numVertices; i++) {
            printf("%d ", tsort[i]);
        }
        printf("\n");
    } else {
        printf("No se puede graf cíclico.\n");
    }

    return 0;
}



// EJERCICIO 6

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define EDIFICIOS 4
#define PISOS 5
#define ALAS 2
#define AULAS 25
#define BLOQUES 85

#define TOTAL (EDIFICIOS * PISOS * ALAS * AULAS * BLOQUES)

int INscriptos[TOTAL];
int CAPACIDAD[TOTAL];

int calcularIndice5D(int e, int p, int a, int au, int b) {
    return ((((e * PISOS + p) * ALAS + a) * AULAS + au) * BLOQUES + b);
}

void cargarDatos() {
    srand(time(NULL));
    for (int i = 0; i < TOTAL; i++) {
        CAPACIDAD[i] = rand() % 101 + 20; 
        INscriptos[i] = rand() % (CAPACIDAD[i] + 1);
    }
}

void aulaBloqueMayorOcupacion() {
    int max_idx = 0;
    double max_porcentaje = 0.0;
    for (int i = 0; i < TOTAL; i++) {
        if (CAPACIDAD[i] > 0) {
            double porcentaje = (double)INscriptos[i] / CAPACIDAD[i];
            if (porcentaje > max_porcentaje) {
                max_porcentaje = porcentaje;
                max_idx = i;
            }
        }
    }
    printf("Aula/bloque mayor ocupacion: indice %d, porcentaje %.2f%%\n", max_idx, max_porcentaje * 100);
}
void promedioAlumnosPorPiso(int bloque) {
    for (int piso = 0; piso < PISOS; piso++) {
        int suma = 0;
        int cantidad = 0;
        for (int edif = 0; edif < EDIFICIOS; edif++) {
            for (int ala = 0; ala < ALAS; ala++) {
                for (int aula = 0; aula < AULAS; aula++) {
                    int idx = calcularIndice5D(edif, piso, ala, aula, bloque);
                    suma += INscriptos[idx];
                    cantidad++;
                }
            }
        }
        double promedio = (double)suma / cantidad;
        printf("Piso %d: %.2f alumnos\n", piso, promedio);
    }
}
void cantidadAlumnosPorAla(int edificio, int piso, int bloque) {
    int por_ala[ALAS] = {0};
    for (int ala = 0; ala < ALAS; ala++) {
        for (int aula = 0; aula < AULAS; aula++) {
            int idx = calcularIndice5D(edificio, piso, ala, aula, bloque);
            por_ala[ala] += INscriptos[idx];
        }
    }
    printf("Alumnos en edificio %d, piso %d, bloque %d:\n", edificio, piso, bloque);
    printf("  Norte: %d\n", por_ala[0]);
    printf("  Sur: %d\n", por_ala[1]);
}

int main() {
    clock_t inicio, fin;
    double tiempo;

    cargarDatos();

    inicio = clock();
    aulaBloqueMayorOcupacion();
    fin = clock();
    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("Tiempo mayor ocupacion: %.6f\n", tiempo);

    inicio = clock();
    promedioAlumnosPorPiso(10);
    fin = clock();
    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("Tiempo promedio por piso: %.6f \n", tiempo);

    inicio = clock();
    cantidadAlumnosPorAla(2, 3, 20);
    fin = clock();
    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    printf("Tiempo alumnos por ala: %.6f \n", tiempo);

    return 0;
}


// EJERCICIO 7

/*
despertar lavarsedientes
despertar vestirse
lavarsedientes desayunar
vestirse desayunar
desayunar salir
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NODOS 100

typedef struct NodoGrafo {
    int destino;
    struct NodoGrafo* siguiente;
} NodoGrafo;

typedef struct {
    NodoGrafo* lista_ady[MAX_NODOS];
    int grado_entrada[MAX_NODOS];
    char* nombres_nodos[MAX_NODOS];
    int num_nodos;
} Grafo;


void inicializar_grafo(Grafo* g) {
    g->num_nodos = 0;
    for (int i = 0; i < MAX_NODOS; i++) {
        g->lista_ady[i] = NULL;
        g->grado_entrada[i] = 0;
        g->nombres_nodos[i] = NULL;
    }
}
int buscar_indice_nodo(Grafo* g, const char* nombre) {
    for (int i = 0; i < g->num_nodos; i++) {
        if (strcmp(g->nombres_nodos[i], nombre) == 0) {
            return i;
        }
    }
    return -1;
}

int agregar_nodo(Grafo* g, const char* nombre) {
    if (buscar_indice_nodo(g, nombre) != -1) {
        return 0;
    }
    
    int indice = g->num_nodos++;
    g->nombres_nodos[indice] = strdup(nombre);
    return 1;
}

void agregar_arista(Grafo* g, const char* origen, const char* destino) {
    int idx_origen = buscar_indice_nodo(g, origen);
    int idx_destino = buscar_indice_nodo(g, destino);
    
    if (idx_origen == -1 || idx_destino == -1) {
        fprintf(stderr, "Error: Nod no encontrado\n");
        return;
    }
    
    NodoGrafo* nuevo = (NodoGrafo*)malloc(sizeof(NodoGrafo));
    nuevo->destino = idx_destino;
    nuevo->siguiente = g->lista_ady[idx_origen];
    g->lista_ady[idx_origen] = nuevo;
    
    g->grado_entrada[idx_destino]++;
}
int topological_sort(Grafo* g, int* resultado) {
    int cola[MAX_NODOS];
    int frente = 0, final = -1;
    int contador = 0;
    for (int i = 0; i < g->num_nodos; i++) {
        if (g->grado_entrada[i] == 0) {
            cola[++final] = i;
        }
    }
    
    while (frente <= final) {
        int actual = cola[frente++];
        resultado[contador++] = actual;
        
        NodoGrafo* temp = g->lista_ady[actual];
        while (temp != NULL) {
            int vecino = temp->destino;
            if (--g->grado_entrada[vecino] == 0) {
                cola[++final] = vecino;
            }
            temp = temp->siguiente;
        }
    }
    
    if (contador != g->num_nodos) {
        return 0;// ciclo
    }
    return 1; 
}
void leer_grafo(const char* filename, Grafo* g) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error al abrir archivo");
        exit(1);
    }
    
    char linea[256];
    while (fgets(linea, sizeof(linea), file)) {
        char origen[50], destino[50];
        
        if (sscanf(linea, "%s %s", origen, destino) == 2) {
            if (buscar_indice_nodo(g, origen) == -1) {
                agregar_nodo(g, origen);
            }
            if (buscar_indice_nodo(g, destino) == -1) {
                agregar_nodo(g, destino);
            }
            
            agregar_arista(g, origen, destino);
        }
    }
    
    fclose(file);
}
int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Uso: %s archivo_grafo.txt\n", argv[0]);
        return 1;
    }
    
    Grafo g;
    inicializar_grafo(&g);
    leer_grafo(argv[1], &g);
    
    int resultado[MAX_NODOS];
    if (topological_sort(&g, resultado)) {
        printf("Orden topologico:\n");
        for (int i = 0; i < g.num_nodos; i++) {
            printf("%d. %s\n", i+1, g.nombres_nodos[resultado[i]]);
        }
    } else {
        printf("El grafo contiene ciclos, no se puede ordenar topologicamente.\n");
    }
    
    for (int i = 0; i < g.num_nodos; i++) {
        NodoGrafo* temp = g.lista_ady[i];
        while (temp != NULL) {
            NodoGrafo* siguiente = temp->siguiente;
            free(temp);
            temp = siguiente;
        }
        free(g.nombres_nodos[i]);
    }
    
    return 0;
}