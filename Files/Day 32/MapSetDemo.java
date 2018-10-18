import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.Hashtable;

public class MapSetDemo {

	public static void main(String[] args) {
	
		System.out.println("HashMap");
		Map<String, String> myMap = new HashMap<>();
		
		myMap.put("Name ", "Ashwini");
		myMap.put("Roll No", "55");
		myMap.put("Y.O.B.", "1996");
		
		System.out.println(myMap);
		// or
		
		Set<String> keys = myMap.keySet();
		for(String i:keys)
			System.out.println(i+" : "+myMap.get(i));
		
		
		//HashMap is not synchronized. 
		//HashTable is synchronized.
		System.out.println("HashTable");
		Map<String, String> yourMap = new Hashtable<>();
		
		yourMap.put("Name", "Ashwini");
		yourMap.put("Roll No", "55");
		yourMap.put("Y.O.B.", "1996");
		
		System.out.println(yourMap);
		Set<String> youKey = yourMap.keySet();
		for(String ii: youKey)
			System.out.println(ii+ ":"+yourMap.get(ii));

	}// end of main
}//end of MapSetDemo
