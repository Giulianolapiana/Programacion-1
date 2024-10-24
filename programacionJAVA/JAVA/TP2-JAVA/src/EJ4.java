import java.util.Scanner;

/*Escribe un programa que pida al usuario su peso en kilogramos y su altura en metros, y luego
calcule su Índice de Masa Corporal (IMC). Imprime una recomendación basada en el IMC (bajo
peso, peso normal, sobrepeso, obesidad).*/
public class EJ4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int kilos;
        System.out.println("Escribe tu peso en kg: ");
        kilos = sc.nextInt();
        System.out.println("Escribe tu altura en metros: ");
        double metros = sc.nextDouble();
        System.out.println("su ICM es de: " + (kilos/(metros*metros)));
    }
}
