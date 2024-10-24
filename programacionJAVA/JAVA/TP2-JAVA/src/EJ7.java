import java.util.Scanner;
/*Escribe un programa que pida al usuario su estado de ánimo (feliz, triste, enérgico, relajado) y luego
recomiende una actividad basada en su estado de ánimo.*/
public class EJ7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String categoria;
        System.out.println("Escribe tu estado de animo (feliz, triste, enérgico, relajado): ");
        categoria = sc.nextLine();
        switch (categoria){
            case "feliz":
                System.out.print("Te recomiendo salir al parque");
                break;
            case "triste":
                System.out.println("Te recomiendo ver una pelicula");
                break;
            case "energico":
                System.out.println("Te recomiendo ir al gimnacio");
                break;
            case "relajado":
                System.out.println("Te recomiendo ver una serie");
                break;
            default:
                System.out.println("categoria no encontrada ");
        }
    }
}
