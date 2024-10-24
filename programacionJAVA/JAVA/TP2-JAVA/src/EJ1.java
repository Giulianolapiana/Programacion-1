import java.util.Scanner;
/*Ejercicio 1: Sistema de Recomendación de Películas
Escribe un programa que pida al usuario su género de película favorito (acción, comedia, drama,
ciencia ficción) y luego recomiende una película basada en su elección.*/

public class EJ1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String pelicula;
        System.out.println("escribi tu genero de pelicula favorito");
        pelicula = sc.nextLine();
        switch (pelicula){
            case "accion":
                System.out.println("Batman el cabellero de la noche");
                break;
            case "comedia":
                System.out.println("son como niños");
                break;
            case "terror":
                System.out.println("La llorona");
                break;
            case "romance":
                System.out.println("avenida brasil");
                break;
            default:
                System.out.println("Genero no encontrado");
        }
    }
}
