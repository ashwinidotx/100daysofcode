public class OnesInBinary {
	
	public int ones(int x) {
		
		int sum = 0;
		while(x>0){
			sum += x%2;
			x=x/2;
			//sum += x^1; // bitwise and
			//x>>=1;
		}
		
		return sum;
	}
	
	public void generate(int range) {
		for(int i=1;i<=range;i++) {
			int sum = 0;
			int x=i;
			while(x>0) {
				sum+=x%2;
				x=x/2;
			}
			System.out.println(i+" contains "+sum+" ones.");
		}
	}
	
	public static void main(String[] args) {
		OnesInBinary onesInBinary = new OnesInBinary();
		System.out.println(" 2 contains: "+onesInBinary.ones(2));
		System.out.println(" 6 contains: "+onesInBinary.ones(6));
		System.out.println("15 contains: "+onesInBinary.ones(15));
		System.out.println("16 contains: "+onesInBinary.ones(16));
		System.out.println("19 contains: "+onesInBinary.ones(19));
		System.out.println("63 contains: "+onesInBinary.ones(63));
		
		System.out.println("------------------------------------");
		onesInBinary.generate(32);
	}
}
