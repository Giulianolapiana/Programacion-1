//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import javax.swing.JOptionPane;
public class Main {
    public static void main( String[] args ){
        String nombre = "";
        nombre = JOptionPane.showInputDialog("Escribe tu nombre");
        String msg = "Hola " + nombre + "!";
        JOptionPane.showMessageDialog(null, msg);
    }
}