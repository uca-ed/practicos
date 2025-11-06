#include <stdio.h>
#include <math.h>
#define MAX 100

//EJERCICIO 1 -(a). Detectar la altura del arbol sin hacer recorridos

int altura(int cantidadNodos, int grado){
    int h = 0;
    int nivelNodos = 1; //el nivel 0 es la raiz
    int total = 1;

    while(total < cantidadNodos){
        h++;
        nivelNodos = nivelNodos * grado;
        total = total + nivelNodos;

    }
    return h;

}
'''
teoria: 
Un árbol de grado m y altura h (lleno o completo hasta cierto nivel)
tiene esta cantidad total de nodos:

𝑁 = 1+𝑚+(m^2)+(m^3)+⋯+(𝑚^h), suma geometrica donde 1 = m^0, osea es la raiz. m es cantHijos nivel 1, m^2 nivel 2, y asi sucesivamente
'''

//EJERCICIO 1 - (b). Algoritmo que realiza un barrido pre-orden

void preOrden(char Arbol[], int grado, int cantidadNodos){
    int S[MAX]; 
    int top = -1;
    int x;

    S[++top] = 0; //esta es la raiz

    while(top>= 0){
        x = S[top--]; //acá desapilo
        printf("%c" , Arbol[x]); //aca visito el nodo y lo printeo, %c porque asumo que el arbol esta compuesto por nodos con char.

        //ahora acá apilo hijos de derecha a izquierda
        
        for(int i = grado; i >= 1; i--){
            int hijo = grado * x + i;  //esta formula me da la posicion del i-esimo hijo en el arreglo.
            
            if(hijo < cantidadNodos){ //evita que acceda más allá del arreglo, lo que me permite.
                S[++top] = hijo;  // S<- R(x), apilo hijos de derecha a izquierda.
            }
        }

    }
}






