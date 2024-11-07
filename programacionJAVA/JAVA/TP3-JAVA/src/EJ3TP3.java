import java.util.Scanner;

public class EJ3TP3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el número de productos: ");
        int numProductos = scanner.nextInt();

        for (int i = 1; i <= numProductos; i++) {
            System.out.print("Ingresa la cantidad disponible del producto " + i + ": ");
            int cantidad = scanner.nextInt();
            if (cantidad < 5) {
                System.out.println("Pedido necesario para el producto " + i + " (unidades disponibles: " + cantidad + ")");
            }
        }
        scanner.close();
    }
}
 