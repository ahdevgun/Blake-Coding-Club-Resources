/**
 * A Cipher that encrypts all ascii text (no quotes)!
 *
 * @author Josh Smith
 * @version 0.0.1
 * 
 * 2.16.21
 */

import java.util.*; // Docs: https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html

public class Main
{
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in); // Initialize scanner
        System.out.print("Text to be encrypted (No Quotes): ");
        String quote = in.nextLine(); // Get user input
        
        System.out.print("Shift Number (Integer): ");
        int shiftNum = Integer.parseInt(in.nextLine()); // Get user input and turn to int
        
        String alphabet = " !#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
        String[] alphaArray = alphabet.split("");
        
        String[] array = quote.split(""); // Create array of user input with item for each character
        String encrypted = "";
        for (int i = 0; i < array.length; i++) { // Loop through all characters to be encrypted
            if (alphabet.indexOf(array[i])+ shiftNum < alphaArray.length) { // 'shiftNum' is cipher translation (forward in 'alphabet')
                encrypted += alphaArray[alphabet.indexOf(array[i])+shiftNum];
            } else {
                encrypted += alphaArray[alphabet.indexOf(array[i])+shiftNum - alphaArray.length]; // Loop back to start for last characters
            }
        }
        
        System.out.println(encrypted); // Print cipher output
    }
}
