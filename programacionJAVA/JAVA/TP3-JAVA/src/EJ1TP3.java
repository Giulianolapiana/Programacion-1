import java.util.Scanner;
/**/
public class EJ1TP3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalHoras = 0;
        String[] actividades = {"Estudio", "Ejercicio", "Lectura", "Tiempo Libre"};
        int i = 0;

        while (i < actividades.length) {
            System.out.print("Ingresa las horas dedicadas a " + actividades[i] + ": ");
            int horas = scanner.nextInt();
            totalHoras += horas;
            i++;
        }

        System.out.println("Tiempo total dedicado a actividades: " + totalHoras + " horas");
        scanner.close();

    }
}
