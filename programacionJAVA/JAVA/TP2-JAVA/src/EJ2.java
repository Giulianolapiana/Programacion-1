/*Escribe un programa que pida al usuario el precio de un producto y la categoría del cliente
(estudiante, adulto, jubilado). Aplica un descuento del 10% para estudiantes, 5% para adultos y
15% para jubilados. Imprime el precio final después del descuento.*/

import java.util.Scanner;

public class EJ2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int producto;
        String categoria;
        System.out.println("Escribe el precio de un producto: ");
        producto = sc.nextInt();
        System.out.println("Escribe la categoria que tienes (estudiante, adulto, jubilado): ");
        sc.nextLine();
        categoria = sc.nextLine();
        switch (categoria){
            case "estudiante":
                System.out.print("El precio es de: " + (producto*0.90));
                break;
            case "adulto":
                System.out.println("El precio es de: " + (producto*0.95));
                break;
            case "jubilado":
                System.out.println("El precio es de: " + (producto*0.85));
                break;
            default:
                System.out.println("categoria no encontrada ");
        }
    }
}
