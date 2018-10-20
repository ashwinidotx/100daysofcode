
public class Flight {

	private int passengers;	
	private int seats;
	
	public Flight() {
		//Set initial state for the flight.
		seats=150;
		passengers=0;
	}
	
	public void add1Passenger() {
		if(passengers<seats)
			passengers+=1;
		else
			handletoomany();
	}
	
	private void handletoomany() {
		System.out.println("Too many Passengers.");
	}
	
	public boolean hasRoom(Flight f2) {
		int total = passengers+f2.passengers;
		return total<=seats;
	}
	
	public Flight createNewWithBoth(Flight f2) {
		Flight newFlight = new Flight();
		newFlight.seats = seats;
		newFlight.passengers = this.passengers+f2.passengers;
		return newFlight;
	}
	
	public int getSeats() {
		return seats;
	}
	
	public void setSeats(int seats) {
		this.seats = seats;
	}
	//--------------MAIN------------------//
	public static void main(String []args) {
	
		Flight lax1 = new Flight();
		Flight lax2 = new Flight();
		//add passengers to both file
		System.out.println("Lax1:"+lax1.getSeats());
		System.out.println("Lax2:"+lax2.getSeats());
		
		Flight lax3=null;
		if(lax1.hasRoom(lax2))
			lax3 = lax1.createNewWithBoth(lax2);
		
		if (lax3!=null)
			System.out.println("Flights were Combined!");
	
		Flight slcToNyc = new Flight();
		slcToNyc.setSeats(270);
		System.out.println("Slc To Nyc:"+slcToNyc.getSeats());
		
		passengers bob = new passengers();
		bob.setCheckedBags(3);
		passengers jane = new passengers(2);
		jane.setCheckedBags(3);
		
	}//end of main
	
}//end of class Flight
