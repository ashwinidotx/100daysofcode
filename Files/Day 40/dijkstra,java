import java.util.Scanner;

public class dijkstra {

	public static void Dijkstra(int[][] adjMatrix) {
		int v = adjMatrix.length;
		boolean visited[] = new boolean[v];
		int distance[] = new int[v];
		distance[0]=0;
		
		for(int i=1;i<v;i++)
			distance[i]=Integer.MAX_VALUE;
		
		for(int i=0;i<v-1;i++)
		{	
			//get the Vertex with minimum distance
			int minVertex = findMinVertex(distance,visited);
			visited[minVertex]=true;
			//Check neighbors.
			for(int j=0;j<v;j++)
			{
				if(adjMatrix[minVertex][j] != 0 && !visited[j] && distance[minVertex]!=Integer.MIN_VALUE)
				{
					int newDist = distance[minVertex] + adjMatrix[minVertex][j];
					if(newDist<distance[j])
						distance[j]=newDist;
				}
			}
			
		}
		//Print the Values:
		
		for(int i=0; i<v; i++)
		{
			System.out.println(i+" : "+distance[i]);
		}
		
	}//end of Dijkstra class
	
	private static int findMinVertex(int[] distance, boolean[] visited) {
		
		int minVertex = -1;
		for(int i=0;i<distance.length;i++)
		{
			if(!visited[i] && (minVertex == -1 || distance[i] < distance[minVertex]))
				minVertex = i;
		}
		return minVertex;
	}
	
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		
		int v = s.nextInt();
		int e = s.nextInt();
		int adjMatrix[][] = new int[v][v];
		
		for(int i=0;i<e;i++)
		{
			int v1 = s.nextInt();
			int v2 = s.nextInt();
			int weight = s.nextInt();
			
			adjMatrix[v1][v2] = weight;
			adjMatrix[v2][v1] = weight;			
		}
		Dijkstra(adjMatrix);
		s.close();
	}//end of main
}// end of dijkstra class