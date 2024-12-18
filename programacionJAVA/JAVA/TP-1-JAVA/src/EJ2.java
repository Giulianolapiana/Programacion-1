/*Escribe un programa que pida al usuario su peso en kilogramos, la duración del ejercicio en
minutos y el tipo de ejercicio (correr, nadar, andar en bicicleta), y luego calcule e imprima las calorías quemadas. Utiliza diferentes tasas de calorías quemadas por minuto para cada tipo de ejercicio*/

import java.util.Scanner;

public class EJ2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ejercicio;
        int peso, duracion;

        System.out.print("Ingrese su peso en Kg: ");
        peso = sc.nextInt(); //leer el peso
        System.out.print("Ingrese la cantidad de minutos de ejercicio: ");
        duracion = sc.nextInt();
        sc.nextLine(); //limpiar el buffer de entrada
        System.out.print("Que tipo de ejercicio realizo(correr, nadar, bicicleta): ");
        ejercicio = sc.nextLine();



        System.out.println("Datos introducidos");
        System.out.println("peso: " + peso);
        System.out.println("duracion: " + duracion);
        System.out.println("ejercicio: " + ejercicio);
        System.out.println("La cantidad de calorias quemadas es " + String.format("%.2f", caloriasQuemadas) + " cal");

    }
}
