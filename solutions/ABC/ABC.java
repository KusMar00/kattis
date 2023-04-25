import java.util.*;

public class ABC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String intLine = sc.nextLine();
        String orientation = sc.nextLine();
        
        String[] intLineArray = intLine.split(" ");
        int[] intArray = new int[3];
        for(int i = 0; i < 3; i++) {
            intArray[i] = Integer.parseInt(intLineArray[i]);
        }
        Arrays.sort(intArray);
        int A = intArray[0];
        int B = intArray[1];
        int C = intArray[2];
        
        char[] oriArray = orientation.toCharArray();
        for (char c: oriArray) {
            if (c == 'A') {
                System.out.print(A + " ");
            } else if (c == 'B') {
                System.out.print(B + " ");
            } else if (c == 'C') {
                System.out.print(C + " ");
            }
        }
    }
}