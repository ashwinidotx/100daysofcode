import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetDemo {
    // Set is an Interface
    // so in order to make an object of set, find a class that implements set -
    // HashSet
    public static void main(String[] args) {
        
        System.out.println("HashSet:");
        Set<Integer> mySet = new HashSet<>();

        mySet.add(92);
        mySet.add(5);
        mySet.add(69);
        mySet.add(55);
        mySet.add(69);

        for (int i : mySet)
            System.out.println(i);
        // When we print the set, it gets printed in a random manner;
        // the reason behind that is there's a fetch method that calls all
        // the saved location. (nearest address first).

        // use TreeSet to sort in ascending order automatically.
        System.out.println("TreeSet:");
        Set<Integer> myTree = new TreeSet<>();

        myTree.add(92);
        myTree.add(5);
        myTree.add(69);
        myTree.add(55);
        myTree.add(69);

        for (int t : myTree)
            System.out.println(t);

    }// end of main
}// end of SetDemo
