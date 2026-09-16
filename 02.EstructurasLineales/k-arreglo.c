#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define D0 4
#define D1 5
#define D2 2
#define D3 25
#define D4 85

#define TOTAL_ELEMENTOS (D0 * D1 * D2 * D3 * D4)
#define A 85  // cuanto mide un aula completa en el arreglo plano

int h(int d0,int d1,int d2,int d3,int d4){
    return d0 * (D1 * D2 * D3 * D4) + d1 * (D2 * D3 * D4) + d2 * (D3 * D4) + d3 * (D4) + d4; 
}

void indice_a_coord(int k, int *d0, int *d1, int *d2, int *d3, int *d4) {
    int stride_d0 = D1 * D2 * D3 * D4; // 21250
    int stride_d1 = D2 * D3 * D4;      // 4250
    int stride_d2 = D3 * D4;           // 2125
    int stride_d3 = D4;                // 85

    *d0 = k / stride_d0;
    int r0 = k % stride_d0;

    *d1 = r0 / stride_d1;
    int r1 = r0 % stride_d1;

    *d2 = r1 / stride_d2;
    int r2 = r1 % stride_d2;

    *d3 = r2 / stride_d3;
    *d4 = r2 % stride_d3;
}
void cargar_datos(int *inscriptos, int *capacidad){
    //con el bucle for recorres cada aula con saltos de a 85
    for(int aula = 0; aula < TOTAL_ELEMENTOS; aula += A){
        //ponemos una capacidad al aula de entre 30 y 50 bancos
        int cap = 30 + rand() % 51; //rand() % 51 devuelve un numero randos entre 0 y 50
        for(int b=0;b<D4;b++){
            int pos = aula + b;
            capacidad[pos] = cap;
            inscriptos[pos] = rand() % (cap+1); //Una cantidad random de inscriptos menor al cap
        }
    }
}

//PREGUNTA A
//Calcula el porcentaje y almacena la posición k
//donde se da el mayor porcentaje. 
//Se utiliza la funcion indice_a_coord() para pasar del arreglo unidimensional de vuelta
//a múltiples dimensiones.
void calcularPromedio(int *inscriptos, int *capacidad){
    double max_porcentaje = -1.0;
    int mejor_k = -1;

    for (int k = 0;k < TOTAL_ELEMENTOS; k++){
        if(capacidad[k] > 0){
            double pct = ((double)inscriptos[k] / (double)capacidad[k]) * 100;
            if(pct > max_porcentaje){
                max_porcentaje = pct;
                mejor_k = k;
            }
        }
    }

    int edif, piso, ala, aula, bloque;
    indice_a_coord(mejor_k,&edif,&piso,&ala,&aula,&bloque);

    printf("\n--- Mayor Porcentaje de Ocupacion ---\n");
    printf("Edificio: %d | Piso: %d | Ala: %s | Aula: %d | Bloque: %d\n",
           edif, piso, (ala == 0 ? "Norte" : "Sur"), aula, bloque);
    printf("Ocupacion: %.2f%% (%d / %d alumnos)\n",
           max_porcentaje, inscriptos[mejor_k], capacidad[mejor_k]);
}

//PREGUNTA B
//cada edificio tiene un piso, que va a tener un ala, que va a tener un aula
//que va a tener un bloque horario. Entonces recorro cada uno con un for, y dentro
//de las aulas busco las posiciones que correspondan con el bloque. 
//Voy sumando los alumnos en cada uno de estas aulas y la cantidad de las aulas funcionando 
//cual contador, luego se calcula el promedio.

void promedioAlumnosPorPiso(int *inscriptos, int bloque){
    //calculo para cada piso de 0 a 4
    printf("\n--- Promedio de alumnos por piso ---\n");
    for (int piso = 0;piso < D1;piso++){
        int suma_alumnos = 0;
        int cantidad_aulas = 0;

        for (int edif=0;edif<D0;edif++){
            for(int ala = 0;ala<D2;ala++){
                for(int aula = 0;aula<D3;aula++){
                    int k = h(edif,piso,ala,aula,bloque);
                    suma_alumnos += inscriptos[k];
                    cantidad_aulas++;
                }
            }
        }
        double promedio = (double)suma_alumnos / cantidad_aulas;
        printf("Piso %d: %.2f alumnos promedio por aula (Total evaluadas: %d aulas)\n", 
               piso, promedio, cantidad_aulas);
    }
}

// PREGUNTA C
// Una lógica similar a la del punto b, solo que acá ya casi todos los datos
//son pasados por parámetro, solo se requiere recorrer las aulas en cada
//ala. 
void alumnosPresentes(int *inscriptos, int edificio, int piso, int bloque){
    int suma_alumnos_norte = 0;
    int suma_alumnos_sur = 0;
    for(int ala = 0;ala<D2;ala++){
        for(int aula = 0;aula<D3;aula++){
            int k = h(edificio, piso, ala, aula, bloque);
            if (ala == 0){
                suma_alumnos_norte += inscriptos[k];
            }else{
                suma_alumnos_sur += inscriptos[k];
            }
        }
    }
    printf("\n--- Alumnos presentes en cada ala ---\n");
    printf("En el ala Norte %d\n", suma_alumnos_norte);
    printf("En el ala Sur %d", suma_alumnos_sur);
} 


int main(void) {
    int *INSCRIPTOS = (int *) malloc(TOTAL_ELEMENTOS * sizeof(int));
    int *CAPACIDAD = (int*) malloc(TOTAL_ELEMENTOS * sizeof(int));

    if (INSCRIPTOS == NULL || CAPACIDAD == NULL){
        printf("No hay suficiente memoria.");
        return 1;
    }

    cargar_datos(INSCRIPTOS,CAPACIDAD);
    calcularPromedio(INSCRIPTOS, CAPACIDAD);
    promedioAlumnosPorPiso(INSCRIPTOS,15);
    alumnosPresentes(INSCRIPTOS, 1, 2, 10);

    return 0;
}
