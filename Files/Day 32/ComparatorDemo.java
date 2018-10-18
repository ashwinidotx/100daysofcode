import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class ComparatorDemo {

	public static void main(String[] args) {
		
		List<Integer> value = new ArrayList<>();
		
		value.add(404);
		value.add(596);
		value.add(250);
		value.add(373);
		// AIM: sort the value list in ascending order of their last digits.
		// create an anonymous comparator method and apply the logic.
		//Then call the sort method on the list and give object of comparator
		// you just created.
		
		// Since Comparator is in interface, we cannot create its object.
		Comparator<Integer> c = new Comparator<Integer>() {
			//Comapre method is a must.
			public int compare(Integer i, Integer j) {
				if(i%10>j%10)
					return 1;
				else
					return -1;
			}
		}; 
		
		//now sort the list
		Collections.sort(value, c);
		
		
		//Printing.
		System.out.println("Values: "+value);
		// or
		for(Integer i: value)
			System.out.print(i+" ");
	}
}
