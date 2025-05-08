// EJ 1 

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "cJSON.h" // chequear implementacion


#define MAX_N 10000

int matriz[MAX_N][MAX_N];
int N = 0; // numero real de nodos

void cargarMatriz(const char* path) {
    FILE* file = fopen(path, "r");
    if (!file) {
        perror("No se pudo abrir el archivo");
        exit(EXIT_FAILURE);
    }

    char linea[1024];
    int fila = 0;

    while (fgets(linea, sizeof(linea), file)) {
        int col = 0;
        char* token = strtok(linea, ",\n");
        while (token && col < MAX_N) {
            matriz[fila][col] = atoi(token);
            token = strtok(NULL, ",\n");
            col++;
        }
        fila++;
    }

    fclose(file);
    N = fila;
}

void minimales() {
    printf("Minimales: ");
    for (int j = 0; j < N; j++) {
        bool esMinimal = true;
        for (int i = 0; i < N; i++) {
            if (matriz[i][j] != 0) {
                esMinimal = false;
                break;
            }
        }
        if (esMinimal) printf("%d ", j);
    }
    printf("\n");
}

void maximales() {
    printf("Maximales: ");
    for (int i = 0; i < N; i++) {
        bool esMaximal = true;
        for (int j = 0; j < N; j++) {
            if (matriz[i][j] != 0) {
                esMaximal = false;
                break;
            }
        }
        if (esMaximal) printf("%d ", i);
    }
    printf("\n");
}

void vecindadDerecha(int nodo) {
    printf("Vecindad derecha de %d: ", nodo);
    for (int j = 0; j < N; j++) {
        if (matriz[nodo][j]) {
            printf("%d ", j);
        }
    }
    printf("\n");
}

void vecindadIzquierda(int nodo) {
    printf("Vecindad izquierda de %d: ", nodo);
    for (int i = 0; i < N; i++) {
        if (matriz[i][nodo]) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    cargarMatriz("01.csv");

    minimales();
    maximales();
    vecindadDerecha(0);
    vecindadIzquierda(0);

    return 0;
}

// EJ 2 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "cJSON.h" 

#define MAX 10000

typedef struct {
    char origen[10];
    char destino[10];
} Par;

Par relaciones[MAX];
char nodos[MAX][10];
int num_rel = 0, num_nodos = 0;

bool existeRelacion(const char* a, const char* b) {
    for (int i = 0; i < num_rel; i++) {
        if (strcmp(relaciones[i].origen, a) == 0 && strcmp(relaciones[i].destino, b) == 0) {
            return true;
        }
    }
    return false;
}

bool esReflexiva() {
    for (int i = 0; i < num_nodos; i++) {
        if (!existeRelacion(nodos[i], nodos[i])) return false;
    }
    return true;
}

bool esSimetrica() {
    for (int i = 0; i < num_rel; i++) {
        if (!existeRelacion(relaciones[i].destino, relaciones[i].origen)) return false;
    }
    return true;
}

bool esAntisimetrica() {
    for (int i = 0; i < num_rel; i++) {
        if (strcmp(relaciones[i].origen, relaciones[i].destino) != 0 &&
            existeRelacion(relaciones[i].destino, relaciones[i].origen)) {
            return false;
        }
    }
    return true;
}

bool esTransitiva() {
    for (int i = 0; i < num_rel; i++) {
        const char* a = relaciones[i].origen;
        const char* b = relaciones[i].destino;
        for (int j = 0; j < num_rel; j++) {
            if (strcmp(b, relaciones[j].origen) == 0) {
                const char* c = relaciones[j].destino;
                if (!existeRelacion(a, c)) return false;
            }
        }
    }
    return true;
}

void cargar_json(const char* path) {
    FILE* f = fopen(path, "rb");
    if (!f) {
        perror("No se pudo abrir el archivo");
        exit(1);
    }
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    rewind(f);

    char* data = malloc(len + 1);
    fread(data, 1, len, f);
    data[len] = '\0';
    fclose(f);

    cJSON* json = cJSON_Parse(data);
    cJSON* P = cJSON_GetObjectItem(json, "P");
    cJSON* E = cJSON_GetObjectItem(json, "E");

    cJSON* nodo = NULL;
    cJSON_ArrayForEach(nodo, P) {
        strcpy(nodos[num_nodos++], nodo->valuestring);
    }

    cJSON* key = NULL;
    cJSON_ArrayForEach(key, cJSON_GetObjectItemCaseSensitive(json, "E")->child) {
        const char* origen = key->string;
        cJSON* destinos = key;
        cJSON* dest = NULL;
        cJSON_ArrayForEach(dest, destinos) {
            strcpy(relaciones[num_rel].origen, origen);
            strcpy(relaciones[num_rel].destino, dest->valuestring);
            num_rel++;
        }
    }

    cJSON_Delete(json);
    free(data);
}

int main() {
    cargar_json("01.json");

    bool reflexiva = esReflexiva();
    bool simetrica = esSimetrica();
    bool antisimetrica = esAntisimetrica();
    bool transitiva = esTransitiva();

    printf("Reflexiva: %s\n", reflexiva ? "Sí" : "No");
    printf("Simétrica: %s\n", simetrica ? "Sí" : "No");
    printf("Antisimétrica: %s\n", antisimetrica ? "Sí" : "No");
    printf("Transitiva: %s\n", transitiva ? "Sí" : "No");

    if (reflexiva && simetrica && transitiva)
        printf("\n⇒ Es una Relación de Equivalencia.\n");
    else if (reflexiva && antisimetrica && transitiva)
        printf("\n⇒ Es un Orden Parcial.\n");
    else
        printf("\n⇒ No es ni Relación de Equivalencia ni Orden Parcial.\n");

    return 0;
}

// EJ 3

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX 10000

char* nodos[] = {"A", "B", "C", "D", "E"};
int num_nodos = 5;

int ady[MAX][MAX] = {{ 0, 1, 1, 0, 0 },{ 0, 0, 0, 1, 0 },{ 0, 0, 0, 0, 0 },{ 0, 0, 0, 0, 1 },{ 0, 0, 0, 0, 0 }};

int iNodo(char* nombre) {
    for (int i = 0; i < num_nodos; i++) {
        if (strcmp(nodos[i], nombre) == 0)
            return i;
    }
    return -1;
}

void encontrarCamino(char* inicio, char* fin) {
    int origen = iNodo(inicio);
    int destino = iNodo(fin);

    if (origen == -1 || destino == -1) {
        printf("Nodo inválido\n");
        return;
    }

    bool visitado[MAX] = {false};
    int padre[MAX];
    for (int i = 0; i < MAX; i++) padre[i] = -1;

    int cola[MAX], frente = 0, finq = 0;
    cola[finq++] = origen;
    visitado[origen] = true;

    while (frente < finq) {
        int actual = cola[frente++];

        if (actual == destino) break;

        for (int i = 0; i < num_nodos; i++) {
            if (ady[actual][i] && !visitado[i]) {
                cola[finq++] = i;
                visitado[i] = true;
                padre[i] = actual;
            }
        }
    }

    if (!visitado[destino]) {
        printf("No se encontró camino.\n");
        return;
    }

    int camino[MAX], len = 0, actual = destino;
    while (actual != -1) {
        camino[len++] = actual;
        actual = padre[actual];
    }

    printf("Camino encontrado: ");
    for (int i = len - 1; i >= 0; i--) {
        printf("%s ", nodos[camino[i]]);
    }
    printf("\n");
}

int main() {
    encontrarCamino("C", "E");
    return 0;
}

