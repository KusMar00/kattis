import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String line = sc.nextLine();
        String[] lineArray = line.split(" ");
        
        for (String s: lineArray) {
            for (int i = 0; i < lineArray.length; i++) {
                int counter = 0;
                if (s.equals(lineArray[i])) {
                    counter++;
                    if (counter > 1) {
                        System.out.println("no");
                    }
                }
            }
        }
        
        System.out.println("yes");
    }
}