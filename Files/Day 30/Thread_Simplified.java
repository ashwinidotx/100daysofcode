
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
		
		t1.start();
		try {
			Thread.sleep(100);
		}
		catch(Exception e) {System.out.println(e);}
		t2.start();
		System.out.println("t1 status: alive:"+t1.isAlive());
		System.out.println("t2 status: alive:" + t2.isAlive());
		System.out.println("End Of Program.\nBye !!!");

	} //End of Main
	
} // End of Thread_Simplified Class
