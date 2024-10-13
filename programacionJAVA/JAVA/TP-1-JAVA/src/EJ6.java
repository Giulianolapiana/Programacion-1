/*Escribe un programa que pida al usuario cuántas horas al día puede estudiar y luego genere un
plan de estudio semanal distribuyendo esas horas en diferentes materias.*/
import java.util.Scanner;

public class EJ6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double horas;

        System.out.print("Cuantas horas al dia estudia: ");
        horas = sc.nextDouble();

        if ((horas >= 0 && horas <= 8)) {
            System.out.print("matematica: " + horas/2 +
                    "\nlengua: " + horas/2);
        } else if ((horas >= 9 && horas <= 15)) {
            System.out.print("matematica: " + horas/4 +
                    "\npython: " + horas/4 +
                    "\njava: " + horas/4 +
                    "\nlengua: " + horas/4);
        } else {
            System.out.println("Horas no validas.");
            return;
        }

    }
}
