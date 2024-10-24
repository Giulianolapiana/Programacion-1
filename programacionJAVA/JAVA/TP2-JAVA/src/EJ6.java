import java.util.Scanner;

/*Escribe un programa que pida al usuario cuántas horas al día duerme, cuántas horas al día hace
ejercicio y cuántas comidas saludables consume al día. Luego, imprime una evaluación de sus
hábitos saludables basada en estos datos.*/
public class EJ6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int dormir,ejercicio,comidas,total;
        System.out.println("cuantas horas al dia dormis ");
        dormir = sc.nextInt();
        System.out.println("cuantas horas al dia haces ejercicio ");
        ejercicio = sc.nextInt();
        System.out.println("cuantas comidas saludables comes al dia ");
        comidas = sc.nextInt();
        total = dormir + ejercicio + comidas;
        if (total >= 11){
            System.out.println("usted es saludable ");
        } else if (total >= 8) {
            System.out.println("usted es medianamente saludable ");
        }else{
            System.out.println("usted No es saludable ");
        }
    }
}
