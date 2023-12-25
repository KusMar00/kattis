import java.util.Scanner;

public class Cold{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int num = sc.nextInt();
        
        
        int coldDays = 0;
        for (int i = 0 ; i < num ; i++){
            int temp = sc.nextInt();
            if (temp < 0){
                coldDays++;
            }
        }
        
        System.out.println(coldDays);
    }


}