import java.util.Random;
import java.util.Scanner;
/*Escribe un programa que pida al usuario que elija entre piedra, papel o tijera. Luego, el programa
elige una opción al azar y determina quién gana. Imprime el resultado del juego.*/
public class EJ5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random aleatorio = new Random(System.currentTimeMillis());
        int intAletorio = aleatorio.nextInt(3);
        System.out.println("juguemos piadra, papel o tijera elije tu opcion: ");
        String usuario = sc.nextLine();
        switch (intAletorio){
            case 0:
                System.out.println("Tu rival saco Piedra");
                break;
            case 1:
                System.out.println("Tu rival saco Papel");
                break;
            case 2:
                System.out.println("Tu rival saco Tijera");
                break;
        }
        switch (usuario){
            case "papel":
                if (intAletorio == 0){
                    System.out.print("Ganas el duelo ");
            } else if (intAletorio == 2) {
                    System.out.print("Pierdes el duelo ");
                }else {
                    System.out.print("Empate ");
                }
                break;
            case "piedra":
                if (intAletorio == 2){
                    System.out.print("Ganas el duelo ");
                } else if (intAletorio == 1) {
                    System.out.print("Pierdes el duelo ");
                }else {
                    System.out.print("Empate ");
                }
                break;
            case "tijera":
                if (intAletorio == 1){
                    System.out.print("Ganas el duelo ");
                } else if (intAletorio == 0) {
                    System.out.print("Pierdes el duelo ");
                }else {
                    System.out.print("Empate ");
                }
                break;
            default:
                System.out.println("categoria no encontrada ");
        }
    }
}
