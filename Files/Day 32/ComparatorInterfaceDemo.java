import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

//To sort the elements of a class, you have to implement comparable
//comparable has only 1 method - compareTo()

class studentInfo implements Comparable<studentInfo> {
    String name;
    int rollno, marks;

    public studentInfo(String name, int rollno, int marks) {
        super();
        this.name = name;
        this.rollno = rollno;
        this.marks = marks;
    }// end of constructor

    @Override
    public String toString() {
        return "Student [Roll no: " + rollno + " Name: " + name + ", Marks: " + marks + "]";
    }

    @Override
    public int compareTo(studentInfo s) {
        return rollno > s.rollno ? 1 : -1;
        // return name.length()>s.name.length()?1:-1;
    }

}// end of studentInfo

public class ComparableInterfaceDemo {

    public static void main(String[] args) {

        List<studentInfo> students = new ArrayList<>();
        // Add info.
        students.add(new studentInfo("Ashwini Singh", 3511055, 82));
        students.add(new studentInfo("Abheesta Vemuru", 3511004, 69));
        students.add(new studentInfo("Abinash Beuria", 3511006, 86));
        students.add(new studentInfo("Aditya Moan Singh", 3511014, 85));
        students.add(new studentInfo("Ashutosh Singh", 3511054, 81));

        // Sorting, based on roll no.
        Collections.sort(students);

        for (studentInfo ss : students)
            System.out.println(ss);

    }// end of main
}// end of ComparableInterfaceDemo Class
