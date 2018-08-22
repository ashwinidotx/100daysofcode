
import java.sql.*;

public class jdbcOne{
    public static void main(String[] args) throws Exception
    {
        String url="jdbc:mysql://localhost/YourDatabaseName";
        String user="root";
        String password="yourPassword";

        String query1="select * from student"; // student- your table name.
        String query2="select name from student where branch='CSE'";

        Class.forName("com.mysql.jdbc.Driver");
        Connection conn=DriverManager.getConnection(url,user,password);
        Statement st=conn.createStatement();
        ResultSet rSet=st.executeQuery(query1);

        while(rSet.next())
        {
            int id=rSet.getInt("student_id");
            String name=rSet.getString("name");
            String branch=rSet.getString("branch");
            System.out.println("Student ID: "+id+" Name: "+name+" Branch: "+branch);
        }
        System.out.println("2nd Method for printing The table!");
        rSet.beforeFirst();
        rSet=st.executeQuery(query1);
        while(rSet.next())
		{
			String Execme=rSet.getInt(1)+" : "+rSet.getString(2)+" : "+rSet.getString(3);
			System.out.println(Execme);
		}
        rSet.beforeFirst();
        rSet=st.executeQuery(query2);
        while(rSet.next())
        {
            int id=rSet.getInt("student_id");
            String name=rSet.getString("name");
            System.out.println("Student ID: "+id+" Name: "+name);
        }
        st.close();
        conn.close();
    }
}