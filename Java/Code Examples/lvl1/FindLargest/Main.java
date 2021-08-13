
/**
 * FindLargest prints the highest monthly temperature and corresponding month.
 *
 * @author Josh Smith
 * @version 0.0.1
 * 
 * 2.5.21
 */
public class Main
{
    public static void main(String[] args)
    {
        String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"};
        int[] temps = {18, 26, 38, 50, 55, 67, 73, 75, 67, 46, 37, 29};
        
        int largestIndex = 0;
        
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] > temps[largestIndex]) {
                largestIndex = i; // Sets the new largest
            }
        }
        
        System.out.println(months[largestIndex] + " - " + temps[largestIndex]);
    }
}
