import java.util.Scanner;

public class ListGame{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int counter = 0;
		int i = 2;
		if (isPrime(n)) {
			counter++;
		} else {
			while (i <= n) {
				if (n % i == 0) {
					n /= i;
					counter++;
					i = 2;
				} else {
					if (n % 2 == 0) {
						i += 2;
					} else{
						if (i % 2 == 0) {
							i++;
						} else {
							i += 2;
						}
					}
				}
			}
		}
		System.out.println(counter);
	}
	
	public static boolean isPrime(int n) {

    if (n <= 1)  return false; 
    if (n <= 3)  return true; 
  
    if (n%2 == 0 || n%3 == 0) return false; 
  
    for (int i=5; i*i<=n; i=i+6) 
        if (n%i == 0 || n%(i+2) == 0) 
           return false; 
  
    return true; 
	}
}