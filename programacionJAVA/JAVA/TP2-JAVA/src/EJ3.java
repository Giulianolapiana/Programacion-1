import java.util.Scanner;
/*Escribe un programa que pida al usuario su género de libro favorito (fantasía, misterio, romance,
ciencia ficción) y luego recomiende un libro basado en su elección.*/
public class EJ3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String pelicula;
        System.out.println("escribi tu genero de libro favorito (fantasía, misterio, romance, ciencia ficción)");
        pelicula = sc.nextLine();
        switch (pelicula){
            case "fantasia":
                System.out.println("Batman el cabellero de la noche");
                break;
            case "misterio":
                System.out.println("son como niños");
                break;
            case "romance":
                System.out.println("La llorona");
                break;
            case "ciencia ficcion":
                System.out.println("avenida brasil");
                break;
            default:
                System.out.println("Genero no encontrado");
        }
    }
}
