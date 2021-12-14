import java.util.Scanner;

public class Program {
  public static String password = "CTF{7h15_15_my_j4m}";

  public static void main(String[] args) {
    Scanner localScanner = new Scanner(System.in);
    System.out.printf("Enter password: ", new Object[0]);
    String str = localScanner.nextLine();
    if (str.equals(password)) {
      System.out.println("Congrats, that was the flag!");
    } else {
      System.out.println("Oops, that's not the flag!");
    }
  }
}
