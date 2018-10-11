
class foreground extends Thread{
	public void run() {
		for(int i=0;i<5;i++) {
			System.out.println("In Foreground !!");
			try { Thread.sleep(500);} catch(Exception e) {}
		}
	}
}

class background extends Thread{
	public void run() {
		for(int i=0;i<5;i++) {
			System.out.println("In Background !");
			try { Thread.sleep(500);} catch(Exception e) {}
		}
	}
}


public class ThreadDemo {

	public static void main(String[] args) {
		foreground fore = new foreground();
		background back = new background();
		
		fore.start();
		try { Thread.sleep(10);} catch(Exception e) {}
		back.start();
		// The start method calls run method from the class.
		//Prints the methods content randomly because we ddnt specify their order.
		// in order to remove that, add a delay between the start calls.
		
		
		//fore.status();
		//back.status();
		//the above 2 calls wont work wrt thread and its proper execution.
	}
}
