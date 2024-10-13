/*Escribe un programa que pida al usuario su fecha de nacimiento (en formato DD/MM/AAAA) y luego imprima su signo del zodiaco y un mensaje de horóscopo correspondiente.
*/
import java.util.Scanner;

public class EJ1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar la fecha de nacimiento al usuario
        System.out.print("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ");
        String fechaNacimiento = scanner.nextLine();

        // Separar el día y el mes de la fecha ingresada
        String[] partesFecha = fechaNacimiento.split("/");
        int dia = Integer.parseInt(partesFecha[0]);
        int mes = Integer.parseInt(partesFecha[1]);

        // Determinar el signo del zodiaco
        String signoZodiaco = "";
        String mensajeHoroscopo = "";

        if ((dia >= 21 && mes == 3) || (dia <= 19 && mes == 4)) {
            signoZodiaco = "Aries";
            mensajeHoroscopo = "Hoy es un buen día para empezar nuevos proyectos.";
        } else if ((dia >= 20 && mes == 4) || (dia <= 20 && mes == 5)) {
            signoZodiaco = "Tauro";
            mensajeHoroscopo = "La paciencia será tu mayor aliada hoy.";
        } else if ((dia >= 21 && mes == 5) || (dia <= 20 && mes == 6)) {
            signoZodiaco = "Géminis";
            mensajeHoroscopo = "Mantén una mente abierta para nuevas ideas.";
        } else if ((dia >= 21 && mes == 6) || (dia <= 22 && mes == 7)) {
            signoZodiaco = "Cáncer";
            mensajeHoroscopo = "Escucha tu intuición, te guiará bien.";
        } else if ((dia >= 23 && mes == 7) || (dia <= 22 && mes == 8)) {
            signoZodiaco = "Leo";
            mensajeHoroscopo = "Es un buen día para brillar y mostrar tu creatividad.";
        } else if ((dia >= 23 && mes == 8) || (dia <= 22 && mes == 9)) {
            signoZodiaco = "Virgo";
            mensajeHoroscopo = "Tu atención a los detalles te llevará lejos hoy.";
        } else if ((dia >= 23 && mes == 9) || (dia <= 22 && mes == 10)) {
            signoZodiaco = "Libra";
            mensajeHoroscopo = "Busca el equilibrio en todas tus decisiones.";
        } else if ((dia >= 23 && mes == 10) || (dia <= 21 && mes == 11)) {
            signoZodiaco = "Escorpio";
            mensajeHoroscopo = "No temas expresar tus sentimientos.";
        } else if ((dia >= 22 && mes == 11) || (dia <= 21 && mes == 12)) {
            signoZodiaco = "Sagitario";
            mensajeHoroscopo = "La aventura te espera, sigue tu curiosidad.";
        } else if ((dia >= 22 && mes == 12) || (dia <= 19 && mes == 1)) {
            signoZodiaco = "Capricornio";
            mensajeHoroscopo = "El esfuerzo y la disciplina darán frutos.";
        } else if ((dia >= 20 && mes == 1) || (dia <= 18 && mes == 2)) {
            signoZodiaco = "Acuario";
            mensajeHoroscopo = "Tu originalidad te destacará entre los demás.";
        } else if ((dia >= 19 && mes == 2) || (dia <= 20 && mes == 3)) {
            signoZodiaco = "Piscis";
            mensajeHoroscopo = "La empatía te permitirá ayudar a quienes te rodean.";
        } else {
            System.out.println("Fecha de nacimiento no válida.");
            return;
        }

        // Mostrar el signo del zodiaco y el mensaje de horóscopo
        System.out.println("Tu signo del zodiaco es: " + signoZodiaco);
        System.out.println("Horóscopo: " + mensajeHoroscopo);
    }
}
