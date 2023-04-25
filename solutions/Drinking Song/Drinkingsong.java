import java.util.Scanner;

public class Drink {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = Integer.parseInt(sc.nextLine());
        String drink = sc.nextLine();
        int numVar = num;

        for (int i = 0; i < num; i++) {
            if (numVar-1 == 0) {
                System.out.println("1 bottle of " + drink + " on the wall, 1 bottle of " + drink + ".");
                System.out.println("Take it down, pass it around, no more bottles of " + drink + ".");
            } else if (numVar == 2){
                System.out.println(numVar + " bottles of " + drink + " on the wall, " + numVar + " bottles of " + drink + ".");
                System.out.println("Take one down, pass it around, " + (numVar - 1) + " bottle of " + drink + " on the wall.");
                System.out.println();
            } else {
                System.out.println(numVar + " bottles of " + drink + " on the wall, " + numVar + " bottles of " + drink + ".");
                System.out.println("Take one down, pass it around, " + (numVar - 1) + " bottles of " + drink + " on the wall.");
                System.out.println();
            }
            numVar--;
        }
    }
}