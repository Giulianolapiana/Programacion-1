/*Escribe un programa que pida al usuario la distancia del viaje en kilómetros, el consumo de
combustible del vehículo en litros por kilómetro y el precio del combustible por litro, y luego
calcule e imprima el costo total del viaje.*/

import java.util.Scanner;
public class EJ5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int distancia;
        double consumo, precio;

        System.out.print("Distancia de viaje en km: ");
        distancia = sc.nextInt();
        System.out.print("Consumo de conbustible en litros por km: ");
        consumo = sc.nextDouble();
        System.out.print("Precio del conbustible por litro: ");
        precio = sc.nextDouble();
        double costoViaje;
        costoViaje = distancia * consumo * precio;

        System.out.println("Datos introducidos");
        System.out.println("distancia: " + distancia + " km");
        System.out.println("consumo: " + consumo + " l/km");
        System.out.println("precio del combustible: $" + precio);
        System.out.println("El costo total es de: $" + String.format("%.2f", costoViaje));

    }
}

