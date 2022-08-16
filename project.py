#include <stdio.h>
#include <stdlib.h>
#define numeros_de_empleados 10

int miMenu();

int main(){
 char nombreEmpleados[numeros_de_empleados]= {'A','B','C','D','E','F','G','H','I','J'};
 float hoursWorkedPerEmployee[numeros_de_empleados]= {0,0,0,0,0,0,0,0,0,0};
 int CategoryEmployee[numeros_de_empleados]= {1,1,2,1,2,3,1,1,2,3};
 float sueldoProcesadoporEmpleado[numeros_de_empleados]= {0,0,0,0,0,0,0,0,0,0};
 int miOpcionElegida = 0;
 int numero = 0;
 int miOpcion = 0;
 float agregarHoras = 0;
 float horasTrabajadas = 0;
 float sueldoNeto = 0;
 float acumHorasTrabajadas1 = 0;
 float acumHorasTrabajadas2 = 0;
 float acumHorasTrabajadas3 = 0;
 float promedioHorasTrabajadas1 = 0;
 float promedioHorasTrabajadas2 = 0;
 float promedioHorasTrabajadas3 = 0;
 int cantCategoria1 = 0;
 int cantCategoria2 = 0;
 int cantCategoria3 = 0;
 float mayorSueldo = 0;
 char mayorNombre[numeros_de_empleados];
  
 do{
 miOpcionElegida = miMenu();
 switch (miOpcionElegida){
   case 1:
     printf("Ingrese numero de legajo: ");
     scanf("%i", &numero);
     if(numero>=0 && numero<10){
       printf("Ingrese horas para agregar: ");
       scanf("%f", &agregarHoras);
       for(int i=0; i<numeros_de_empleados; i++){
           if(hoursWorkedPerEmployee[i] == hoursWorkedPerEmployee[numero]){
               hoursWorkedPerEmployee[numero] += agregarHoras/2; //acá los dividi por 2 porque cuando lo imprimía lo multiplicaba por 2
               }
             }
        }
      for(int i=0; i<numeros_de_empleados; i++){
          printf("%.2f ", hoursWorkedPerEmployee[i]);
      }
   break;
   case 2:
     printf("La liquidacion de los sueldos es:\n");
     for(int i=0; i<numeros_de_empleados; i++){
         if(CategoryEmployee[i] == 1){
             sueldoNeto = hoursWorkedPerEmployee[i] * 100;
             sueldoProcesadoporEmpleado[i] += sueldoNeto;
         } else if(CategoryEmployee[i] == 2){
             sueldoNeto = hoursWorkedPerEmployee[i] * 120;
             sueldoProcesadoporEmpleado[i] += sueldoNeto;
         } else if(CategoryEmployee[i] == 3){
             sueldoNeto = hoursWorkedPerEmployee[i] * 150;
             sueldoProcesadoporEmpleado[i] += sueldoNeto;
         }
     }
     for(int i=0; i<numeros_de_empleados; i++){
          printf("%.2f ", sueldoProcesadoporEmpleado[i]);
     }
   break;
   case 3:
   printf("Legajo\tNombre\tHoras trabajadas\tCategoria\tSueldo Neto\t\n");
   for(int i=0; i<numeros_de_empleados; i++){
     printf("\t%i\t\t%c\t\t%.2f\t\t\t\t%i\t\t\t%.2f\n",i,nombreEmpleados[i],hoursWorkedPerEmployee[i],CategoryEmployee[i],sueldoProcesadoporEmpleado[i]);
   }
   break;
   case 4:
     for(int i=0; i<numeros_de_empleados; i++){
         if(CategoryEmployee[i] == 1){
             cantCategoria1++;
             acumHorasTrabajadas1 += hoursWorkedPerEmployee[i];
             promedioHorasTrabajadas1 = acumHorasTrabajadas1/cantCategoria1;
         } else if(CategoryEmployee[i] == 2){
             cantCategoria2++;
             acumHorasTrabajadas2 += hoursWorkedPerEmployee[i];
             promedioHorasTrabajadas2 = acumHorasTrabajadas2/cantCategoria2;
         } else if(CategoryEmployee[i] == 3){
             cantCategoria3++;
             acumHorasTrabajadas3 += hoursWorkedPerEmployee[i];
             promedioHorasTrabajadas3 = acumHorasTrabajadas3/cantCategoria3;
         }
     }
     printf("El promedio de horas de la categoria 1 es de %.2f\n", promedioHorasTrabajadas1);
     printf("El promedio de horas de la categoria 2 es de %.2f\n", promedioHorasTrabajadas2);
     printf("El promedio de horas de la categoria 3 es de %.2f\n", promedioHorasTrabajadas3);
     
   break;
   case 5:
     for(int i=0; i<numeros_de_empleados; i++){
        if(i==0){
             mayorSueldo = sueldoProcesadoporEmpleado[i];
             strcpy(mayorNombre, nombreEmpleados);// no me sale :(
        }
        if(sueldoProcesadoporEmpleado[i] > mayorSueldo){
             mayorSueldo = sueldoProcesadoporEmpleado[i];
             strcpy(mayorNombre, nombreEmpleados);
       }
     }
     printf("El nombre del empleado que mas gano es %c y su sueldo es de %.2f\n", mayorNombre, mayorSueldo);
     
   break;
   default:
     printf("Salio del programa");
   break;
   }
  }while (miOpcionElegida>=1 && miOpcionElegida<=5);
  
 return 0;
}


int miMenu(){
 int miOpcion = 0;
  
 printf("\n1-Ingreso Horas Trabajadas\n");
 printf("2-Procesar Liquidacion de Sueldo\n");
 printf("3-Informe total de empleados\n");
 printf("4-Informe Promedio horas trabajada por categoria\n");
 printf("5-Informe Empleado que mas gana\n");
 printf("6-Salir\n");
 scanf("%d",&miOpcion);
  
 return miOpcion;
}