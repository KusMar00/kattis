import java.util.Scanner;

public class Grass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double cost = sc.nextDouble();
        int num = sc.nextInt();
        double price = 0;
        for (int i = 0; i < num; i++) {
            double sqrm = sc.nextDouble() * sc.nextDouble();
            price += sqrm * cost;
        }
        System.out.println(price);
    }
}