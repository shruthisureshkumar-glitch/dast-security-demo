
import java.util.Scanner;

class Student {
    public void display() {
        System.out.println("Student Object Created Successfully.");
    }
}

class Teacher {
    public void display() {
        System.out.println("Teacher Object Created Successfully.");
    }
}

public class SecureCodingDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.println("==============================");
            System.out.println(" Secure Coding Demonstration");
            System.out.println(" Reflection Misuse Prevention");
            System.out.println(" Exception Handling");
            System.out.println("==============================");

            System.out.println("\nAllowed Objects");
            System.out.println("1. Student");
            System.out.println("2. Teacher");
            System.out.print("\nEnter Object Name: ");

            String choice = sc.nextLine().trim();

            switch (choice.toLowerCase()) {
                case "student":
                    Student s = new Student();
                    s.display();
                    break;

                case "teacher":
                    Teacher t = new Teacher();
                    t.display();
                    break;

                default:
                    throw new IllegalArgumentException(
                        "Unauthorized Object Name Entered."
                    );
            }

            System.out.println("Program Executed Successfully.");

        } catch (IllegalArgumentException ex) {
            System.out.println("Error: " + ex.getMessage());

        } catch (Exception ex) {
            System.out.println("Unexpected Error Occurred.");

        } finally {
            sc.close();
            System.out.println("Scanner Closed Successfully.");
        }
    }
}
