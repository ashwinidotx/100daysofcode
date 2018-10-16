
public class Thread_Simplified {
	// Instead of making a runnable class object, we can 
	// define the method in Thread as parameters.
	
	public static void main(String[] args) {
		
		Thread t1 = new Thread(() ->
		{
			for(int i=0;i<5;i++)
			{
				System.out.println("Value = "+i);
				try {
					Thread.sleep(500);
				}
				catch(Exception e) { System.out.println(e); }
			}
		});
		Thread t2 = new Thread(()-> {
			for(int i=0;i<5;i++)
			{
				System.out.println("Remaining Value = "+(5-i));
				try {
					Thread.sleep(500);
				}
				catch(Exception e) {System.out.println(e);}
			}
		});
		// Setting name.
		t1.setName("Current Value");
		t2.setName("Remainder Value");
		String thread1 = t1.getName(), thread2 = t2.getName();

		// Setting priority.
		System.out.println("Priority:");
		System.out.println(thread1 + " : " + t1.getPriority());
		System.out.println(thread2 + " : " + t2.getPriority());
		System.out.println();

		t1.setPriority(Thread.MIN_PRIORITY);
		t2.setPriority(Thread.MAX_PRIORITY);

		// executing threads.
		t1.start();
		try {
			Thread.sleep(100);
		}
		catch(Exception e) {System.out.println(e);}
		t2.start();
		System.out.println(thread1 + "'s status: Alive: " + t1.isAlive());
		System.out.println(thread2 + "'s status: Alive: " + t2.isAlive());

		System.out.println("End Of Program.\nBye !!!");

	} //End of Main
	
} // End of Thread_Simplified Class
