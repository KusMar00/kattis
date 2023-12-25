import java.util.HashMap;
import java.util.Scanner;

public class Spam {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		sc.close();

		char[] chars = input.toCharArray();
		int[] result = new int[4]; // counter array for [whitespace, lower-case, upper-case, symbol]  

		for (char c : chars) {
			if (c == '_') result[0]++;
			else if (Character.isLowerCase(c)) result[1]++;
			else if (Character.isUpperCase(c)) result[2]++;
			else result[3]++;
		}

		System.out.println(result[0]*1.0/input.length());
		System.out.println(result[1]*1.0/input.length());
		System.out.println(result[2]*1.0/input.length());
		System.out.println(result[3]*1.0/input.length());
	}
}