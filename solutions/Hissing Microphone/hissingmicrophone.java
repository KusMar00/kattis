import java.util.Scanner;

public class Hiss{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        
        if(word.contains("ss")){
            System.out.println("hiss");
        } else{
            System.out.println("no hiss");
        }
    }
}