import java.util.List;
import java.util.ArrayList;

public class ArrayListDemo {

    public static void main(String[] args) throws Exception {

        List value = new ArrayList();
        value.add(55);
        value.add(12);
        value.add(69);
        value.add(2,44);
        value.add("Shady");
        value.add(3.14);
        // Every value stored here is a wrapper class object
        // Integer 45, Integer 69, String "Shady" and so on...
        // so we can use enhanced for loop to print them.
        // The iterator we're gonna use is of object type.
        // so...

        System.out.println("Values: ");
        for (Object i : value) {
            System.out.print(i + " ");
        }
        System.out.println("\nSize: " + value.size());

        System.out.println(value);

    }// end of main
}// end of ArrayListDemo class
