import java.util.Scanner;

public class EJ2TP3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa la cantidad de empleados: ");
        int cantidadEmpleados = scanner.nextInt();
        final int TARIFA = 15;

        for (int i = 1; i <= cantidadEmpleados; i++) {
            System.out.print("Ingresa las horas trabajadas por el empleado " + i + ": ");
            int horas = scanner.nextInt();
            int salario = horas * TARIFA;
            System.out.println("Salario del empleado " + i + ": $" + salario);
        }
        scanner.close();
    }
}
