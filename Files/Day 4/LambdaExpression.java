
interface oneandonly{
	void Display();
}

public class LambdaExpression {

	public static void main(String[] args) {
		
		/* create an instance of the interface.
		 * 
		 * oneandonly obj=new oneandonly(){
		 * 						public void Display(){
		 * 						  System.out.println("Hey");			
		 * 						}
		 * 						};
		 * instance of the above method, we can
		 * use Lambda expression to reduce the amount of
		 * code we have to write. 
		 * this only works with functional interface.
		 */
		oneandonly obj=()-> { System.out.println("Hello there");
							  System.out.println("General Kenobi!");
							};// Lambda Expression!
		obj.Display();
	}
}
