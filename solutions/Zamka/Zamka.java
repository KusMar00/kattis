import java.util.Scanner;

public class Zamka {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lowNum = sc.nextInt();
        int highNum = sc.nextInt();
        int X = sc.nextInt();

        for(int i = lowNum; i <= highNum; i++) {
            int sum = 0;
            int iTemp = i;
            while (iTemp > 0) {
                sum += iTemp % 10;
                iTemp = iTemp / 10;
            }
            if (sum == X) {
                System.out.println(i);
                break;
            }
        }

        for(int i = highNum; i >= lowNum; i--) {
            int sum = 0;
            int iTemp = i;
            while (iTemp > 0) {
                sum += iTemp % 10;
                iTemp = iTemp / 10;
            }
            if (sum == X) {
                System.out.println(i);
                break;
            }
        } 

    }
}