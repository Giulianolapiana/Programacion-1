public class Persona {
    private String nombre;
    private String apellidos;
    private String numeroDocumentoIdentidad;
    private int anioNacimiento;
    private String paisNacimiento;
    private char genero;

    // Constructor
    public Persona(String nombre, String apellidos, String numeroDocumentoIdentidad, int anioNacimiento, String paisNacimiento, char genero) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.numeroDocumentoIdentidad = numeroDocumentoIdentidad;
        this.anioNacimiento = anioNacimiento;
        this.paisNacimiento = paisNacimiento;
        this.genero = genero;
    }

    public void imprimir() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellidos: " + apellidos);
        System.out.println("Número de documento de identidad: " + numeroDocumentoIdentidad);
        System.out.println("Año de nacimiento: " + anioNacimiento);
        System.out.println("Pais de nacimiento: " + paisNacimiento);
        System.out.println("Genero: " + (genero == 'H' ? "Hombre" : "Mujer"));
        System.out.println();
    }

    public static void main(String[] args) {
        Persona p1 = new Persona("Pedro", "Pérez", "1053121010", 1998, "Argentina", 'H');
        Persona p2 = new Persona("Luis", "León", "1053223344", 2001, "Chile", 'M');

        p1.imprimir();
        p2.imprimir();
    }
}
