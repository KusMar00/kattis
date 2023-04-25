import java.util.Scanner;

public class Pot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            int exponent = num % 10;
            int base = num / 10;
            sum += Math.pow(base, exponent);
        }
        System.out.println(sum);
    }
}