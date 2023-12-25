import java.util.*;

public class Alphabet {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Character, String> alphaMap = new HashMap<>();
        
        alphaMap.put('a', "@");
        alphaMap.put('b', "8");
        alphaMap.put('c', "(");
        alphaMap.put('d', "|)");
        alphaMap.put('e', "3");
        alphaMap.put('f', "#");
        alphaMap.put('g', "6");
        alphaMap.put('h', "[-]");
        alphaMap.put('i', "|");
        alphaMap.put('j', "_|");
        alphaMap.put('k', "|<");
        alphaMap.put('l', "1");
        alphaMap.put('m', "[]\\/[]");
        alphaMap.put('n', "[]\\[]");
        alphaMap.put('o', "0");
        alphaMap.put('p', "|D");
        alphaMap.put('q', "(,)");
        alphaMap.put('r', "|Z");
        alphaMap.put('s', "$");
        alphaMap.put('t', "']['");
        alphaMap.put('u', "|_|");
        alphaMap.put('v', "\\/");
        alphaMap.put('w', "\\/\\/");
        alphaMap.put('x', "}{");
        alphaMap.put('y', "`/");
        alphaMap.put('z', "2");
        
        String message = sc.nextLine();
        char[] msArray = message.toCharArray();
        for (char c: msArray) {
            if (alphaMap.containsKey(Character.toLowerCase(c))){
                System.out.print(alphaMap.get(Character.toLowerCase(c)));
            } else {
                System.out.print(c);
            }
        }
        
    }
}