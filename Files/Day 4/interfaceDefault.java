
interface helloThere{
	void show();
	default void ok() {
		System.out.println("in OK.");
	}
}
interface generalKenobi{
	default void ok() {
		System.out.println("Jedi die.");
	}
}


class okayyy implements helloThere,generalKenobi{

	
	public void show() {
		
		System.out.println("Towerdive, We must Towerdive!");
	}
	 public void ok() {
		 System.out.println("Yeti knows the Way.");
		// calling after creating multiple interfaces.
		 generalKenobi.super.ok();
		 helloThere.super.ok();

	 }	
	 
	 
}

public class interfaceDefault {

	public static void main(String[] args) {
		helloThere helloThere=new okayyy();
		helloThere.show();
		helloThere.ok();
	}
}
