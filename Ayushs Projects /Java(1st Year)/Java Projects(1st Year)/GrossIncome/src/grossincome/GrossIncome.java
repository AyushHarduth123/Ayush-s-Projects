/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package grossincome;
import java.util.Scanner;
/**
 *
 * @author ayush
 */
public class GrossIncome {
    
    
     public static void main(String[] args) {
        // One Scanner for all input: two Scanners on System.in can swallow each other's input
        Scanner scan = new Scanner(System.in);

        System.out.println("What are your total hours: ");
        double totHours = scan.nextDouble();

        userInput(scan, totHours);
    }


    //Method Declarations
    public static void userInput(Scanner inp, double hours){
        System.out.println("Enter your hourly rate: ");
        double rate = inp.nextDouble();

        double gross = hours * rate;
        System.out.println("Your Income Information: "
                + "\nRate:"+rate
                + "\nTotal Hours:"+hours
                + "\nYour Gross Income: "+gross);
    }
    
}
