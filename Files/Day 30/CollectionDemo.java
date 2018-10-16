package com.collectionmodule;

import java.util.Collection;
import java.util.Iterator;
import java.util.ArrayList;

public class CollectionDemo {
	
	public static void main(String[] args) {
		
		Collection value = new ArrayList();
		value.add(12);
		value.add(14);
		value.add(1);
		value.add(9);
		
		System.out.println(value);
		System.out.println(value.size());
		System.out.println(value.contains(12));
		System.out.println(value.remove(12));
        System.out.println(value);
        
		//Collection doesn't support index numbers.
		//so we use iterators to iterate over them.
        
        Iterator it = value.iterator();
		
		System.out.println(it.hasNext());
		
		System.out.println("Values:");
		while(it.hasNext())
		{
			System.out.println(it.next());
		}
		
	} //end of main method
	
} //end of CollectionDemo Class
