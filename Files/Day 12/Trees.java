
class Node {
	
	Node left,right;
	int data;
	
	public Node(int data) {
		this.data = data;
	}
	
	public void insert(int value) {
		
		if(value<=data) {
			if(left==null)
				left=new Node(value);
			else 
				left.insert(value);
		}
		else {
			if(right==null)
				right=new Node(value);
			else 
				right.insert(value);			
		}
	}
	
	
	public boolean contains(int value) {
		if(data==value)
			return true;
		else if(value<data){
			if(left==null)
				return false;
			else
				left.contains(value);
		}
		else{
			if(right==null)
				return false;
			else
				right.contains(value);
		}
		return false;
	}
	
	public void printInOrder() {
		if(left!=null)
			left.printInOrder();
		
		System.out.println(data);
		
		if(right!=null)
			right.printInOrder();
	}
}


public class Trees {

	public static void main(String[] args) {
		Node node=new Node(5);
		node.insert(10);
		node.insert(2);
		node.insert(20);
		node.insert(15);
		node.printInOrder();

	}

}
