/*Escribe un programa que pida al usuario su estado de ánimo (feliz, triste, enérgico, relajado) y luego
genere una lista de reproducción con canciones sugeridas para ese estado de ánimo.*/

import java.util.Scanner;

public class EJ4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String estadoAnimo;

        System.out.print("Ingrese su estado de animo (feliz, triste, enérgico, relajado): ");
        estadoAnimo = sc.nextLine();

        switch (estadoAnimo){
            case "feliz":
                System.out.print("Walking on Sunshine – Katrina & The Waves. ...\n" +
                        "Livin' On A Prayer – Bon Jovi. ...\n" +
                        "Girls Just Wanna Have Fun – Cyndi Lauper. ...\n" +
                        "Eye Of The Tiger – Survivor. ...\n" +
                        "Uptown Girl – Billy Joel.");
                break;
            case "triste":
                System.out.print("Good Vibrations – The Beach Boys. ...\n" +
                        "Dancing Queen – Abba. ...\n" +
                        "Don't Stop Me Now – Queen.");
                break;
            case "energico":
                System.out.print("Walking on Sunshine: De Katrina & The Waves \n" +
                        "I Will Survive: De Gloria Gaynor \n" +
                        "Livin' On A Prayer: De Bon Jovi \n" +
                        "Girls Just Wanna Have Fun: De Cyndi Lauper");
                break;
            case "relajado":
                System.out.print("I'm a Believer: De The Monkees \n" +
                        "Eye Of The Tiger: De Survivor \n" +
                        "Uptown Girl: De Billy Joel \n" +
                        "Good Vibrations: De The Beach Boys \n");
                break;
            default:
                System.out.println("Estado de animo no valido");
                return;
        }

    }
}
