/**
ST10365068
ST10301544
ST10281011
ST10380049
**/
package useradressapp;
import java.util.Scanner;



/**
 *
 * @author ayush
 */
public class UserAddressApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner addressData = new Scanner(System.in);
        int houseNumber;
        String strName;
        String city;
        int areaCode;

        
        
        System.out.println("Enter house number: ");
        houseNumber = addressData.nextInt();
        
        
        System.out.println("Enter street name: ");
        strName = addressData.next();
        addressData.nextLine();
        
        System.out.println("Enter city name: ");
        city = addressData.next();
        
        System.out.println("Enter area code: ");
        areaCode = addressData.nextInt();
       
      
//        System.out.println("\nYour address: \t"+ houseNumber +" "+ strName+" Street");
//        System.out.println( "\t\t"+ city);
//        System.out.println( "\t\t"+ areaCode);


       String AddressInfo = "Your address: "+ houseNumber + " " + strName + " Street " + city + " " + areaCode;
        System.out.println(AddressInfo);
        
        

    }
}
