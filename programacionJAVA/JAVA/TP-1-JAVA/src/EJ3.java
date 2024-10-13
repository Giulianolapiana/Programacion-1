/*Escribe un programa que pida al usuario su nivel de condición física (principiante, intermedio,
avanzado) y luego genere una rutina de ejercicio semanal con diferentes tipos de ejercicios y duraciones.*/

import java.util.Scanner;
public class EJ3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String nivel;

        System.out.print("Ingrese su nivel de condicion fisica (principiante, intermedio, avanzado): ");
        nivel = sc.nextLine(); //leer el peso

        switch (nivel){
            case "principiante":
                System.out.print("Pecho: push-ups, flexiones o presses con mancuernas.\n" +
                        "Espalda: dominadas, flies o remo en polea baja.\n" +
                        "Duracion: 20 minutos");
                break;
            case "intermedio":
                System.out.print("Pecho: push-ups, flexiones o presses con mancuernas.\n" +
                        "Espalda: dominadas, flies o remo en polea baja.\n" +
                        "Hombros: press militar, elevaciones laterales o frontales con mancuernas.\n"+
                        "Duracion: 40 minutos");
                break;
            case "avanzado":
                System.out.print("Pecho: push-ups, flexiones o presses con mancuernas.\n" +
                        "Espalda: dominadas, flies o remo en polea baja.\n" +
                        "Hombros: press militar, elevaciones laterales o frontales con mancuernas.\n" +
                        "Tríceps: extensiones tríceps en polea baja o dips.\n" +
                        "Duracion: 60 minutos");
                break;
            default:
                System.out.println("Nivel no valido");
                return;
        }

    }
}
