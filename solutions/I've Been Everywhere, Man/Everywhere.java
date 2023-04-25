import java.util.*;

public class Everywhere{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int iterations = sc.nextInt();

        Set<String> cities = new HashSet<>();
        for(int i = 0 ; i < iterations ; i++){
            
            int n = sc.nextInt();

            for(int j = 0 ; j <= n ; j++){
                String city = sc.nextLine();
                cities.add(city);
            }
            System.out.println(cities.size()-1);
        }
    }
}