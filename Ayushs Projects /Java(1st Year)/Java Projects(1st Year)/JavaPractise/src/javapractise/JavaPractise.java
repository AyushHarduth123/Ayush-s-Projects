/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javapractise;

import java.util.ArrayList;
import java.util.Scanner;
import javax.swing.JOptionPane;
import java.util.Random; // Used for random values 

/**
 *
 * @author ayush
 */
public class JavaPractise {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

       //Expressions();
       // variables();
       // swappingViariables();
       // ExceptingUserInput();
       // JavaAppEx();
       //Scanners();
       //HypotenuseApp();
       //RandomValues();
       //IfStatements();
       Switches();
       //LogicalOpperators();
       //LogicalOpperatorsApp();
       //LogicalOpperatorsAppNOT();
       //WhileLoops();
       //ForLoops();
       //NestedForLoops();
       //Arrays();
       TwoDArrays();
      // StringMethods();
      Arraylists();
      
               
       
       
    }
    
    public static void variables(){
        
        //variables
        //all about variables and how they work 
        /* 
        boolean  true or false
        byte  -128 to 127
        short  -32768 to 32767
        int  -2 bil to 2 bil
        long - 9 quintillion to 9 quintillion
        float Fractional number up to 6-7 gigits ex. 3.141592
        double  Fractional number up to 15 gigits ex. 13.156548896558936
        char  single character/letter/ASCII value ex.'f'
        String a sentance of characters ex. "Hello world!"
        
        Proccess of declaring a variable
        
        declaration  int x;
        assignment   x = 123;
        initialisation int x = 1233;
      
        */
        
        int x = 123; // initialistation
        double y = 3.14;
        boolean z = true;
        char symbol = '@';
        String name = "Bro";
        System.out.println("My number is: "+x);
}
    
    public static void swappingViariables(){
    
        String x = "water";
        String y = "Kool-Aid";
        String temp;//temp temporaraly store variables
        temp = x;
        x = y;
        y=temp;
    
        System.out.println("x: "+x);
        System.out.println("y: "+y);

    }
  
    public static void ExceptingUserInput(){
        Scanner scanner = new Scanner(System.in);
      
        System.out.println("What is your name");
        String name = scanner.nextLine();
        
        
        System.out.println("What is your age?");
        int age = scanner.nextInt();
        scanner.nextLine();
       
        System.out.println("What is your favourite food?");
        String food = scanner.nextLine();
        
        
        
        System.out.println("Hello "+name);
        System.out.println("You are "+age+" years old");
        System.out.println("Your favourite food is "+food);

    }
    
    public static void Expressions(){
    
    //Expresstions are a cominaton of operands and opperators 
    // operands = values, variables, numbers,quantity
    //opperators = + - / * %
    
        double friends = 10;
    
        friends = (double)friends / 3;
        System.out.println(friends);
        
        
    }
    
    public static void JavaAppEx(){
    
    String name = JOptionPane.showInputDialog("Enter your name");
    JOptionPane.showMessageDialog(null, "Hello "+name);
    
    int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age"));
    JOptionPane.showMessageDialog(null,"You are "+age+" years old");
    
    double height = Double.parseDouble(JOptionPane.showInputDialog("Enter in your Hieght"));
    JOptionPane.showMessageDialog(null,"You are "+height+" years old");
    
     
    }
    
    
    public static void Scanners(){
    
        double x = 3.14;
        double y = 10;
       // double z;
        
        /*Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter side x: ");
        x = scanner.nextDouble();
        */
        double z = Math.max(x, y);
        System.out.println(z);
        
        double u = Math.min(x, y);
        System.out.println(u);
        // Abs = absolute value of a number ||
        
// Abs = absolute value of a number ||
        System.out.println(y);
        // sqrt is square root
        
// sqrt is square root 
        System.out.println(y);
        // round is used to round of numbers
        
// round is used to round of numbers
        System.out.println(x);
        // round is used to round up
        
// round is used to round up
        System.out.println(x);
        // round is used to round down

        System.out.println(x);
    }
    
    public static void HypotenuseApp(){
    //HOW TO USE THE MATH CLASS
        double x;
        double y;
        double z;
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter side x: ");
        x = scanner.nextDouble();
        
        System.out.println("Enter side y :");
        y = scanner.nextDouble();
        
        z = Math.sqrt((x*x)+(y*y));
        
        System.out.println("The Hypotenuse is: "+z);
        scanner.close();
    }
    
    public static void RandomValues(){
       
           Random random = new Random();  // random numbers between -2 bil and +2 bil
           
           //int x = random.nextInt(6)+1; // place restrictions in the brackets to restrict the random numbers
           //double y = random.nextDouble();
           boolean z = random.nextBoolean();
           
           System.out.println(z);
           
    }
       
    public static void IfStatements(){
       
           
           // if statements = performs a block of code if condition variables evaluates to be true.
           int age = 3; //== means eqaul to 
           
           if(age >=75)
           {
               System.out.println("Ok Boomer");
           }
           else if (age >=18){
               System.out.println("You are an adult");
           }
           else if (age>=13){
               System.out.println("You are a teenager");
           }
           else if (age==3){
               System.out.println("You are still a child");
           }
           else { 
               System.out.println("You are not an adult");
           }
       }
       
    public static void Switches(){
       
         /*Switch=   statement that allows a variable or other value to be
         tested for eqaultiy against a list of values
        
           We can use these Data Types with Switches
           byte
           short
           char
           int
           String
           
        */
         
         String day = "Friday";
                 
                 switch(day){
                     case "Sunday": System.out.println("It is Sunday");
                     break;
                     case "Monday": System.out.println("It is Monday");
                     break;
                     case "Tuesday": System.out.println("It is Tuesday");
                     break;
                     case "Wednesday": System.out.println("It is Wednesday");
                     break;
                     case "Thursday": System.out.println("It is Thursday");
                     break;
                     case "Friday": System.out.println("It is Friday");
                     break;
                     case "Saturday": System.out.println("It is Saturday");
                     break;
                 
                 }
         
       }    
       
    public static void LogicalOpperators(){
         
            //Logical Opperators = used to connect two or more expresstions
            //      
            //     && = (AND) both conditions MUST be true
            //     || = (OR)  either condition Must be true
            //      ! = (NOT) reverses boolean values of condition
            
            int temp = 25;
            
            if(temp>30){
                System.out.println("It is hot outside");
            }
            else if(temp>=20 && temp<=30){
                System.out.println("It is warm outside");
            }
            else {
                System.out.println("It is cold outside");
            }
        
        }  
    public static void LogicalOpperatorsApp(){
            Scanner scanner = new Scanner(System.in);
            
            System.out.println("You are playing a game, Press q or Q to quit");
            String response = scanner.next();
            
            if(response.equals("q")|| response.equals("Q")){
                System.out.println("You Quit The Game");
            }
            else {
                System.out.println("You are still playing the game pew-pew");
            }
        }
    public static void LogicalOpperatorsAppNOT(){
        Scanner scanner = new Scanner(System.in);
            
            System.out.println("You are playing a game, Press q or Q to quit");
            String response = scanner.next();
            
            if(!response.equals("q")&& !response.equals("Q")){ // Cheching to see if the response is not equal to 'q' AND not equal to 'Q' if that is true the it will execute the program
                System.out.println("You are still playing the game pew-pew");
            }
            else {
                System.out.println("You quit the game");
            }
        }
    public static void WhileLoops(){
        // while loop = executes a block of code as long as it's condition remains true
        
        Scanner scanner = new Scanner(System.in);
        
        String name = "";
        
        while(name.isBlank()){
            System.out.println("Enter your name: "); // will execute this until the prompt has been fufilled
            name = scanner.nextLine();
        }
            System.out.println("Hello "+name);
            
    // do loop
    
        do{
            System.out.println("Enter your name: ");//will frist execute the prompt as long as there is no input
            name = scanner.nextLine();
        }while(name.isBlank());
        
    }
    public static void ForLoops(){
        
        // for loops = executes a block of code a limited amount of times
        
        for(int i = 10; i >= 0; i--){
            System.out.println(i);
        }
            System.out.println("Happy new year");
    }    
    public static void NestedForLoops(){
        
        //nested loop= a loop inside another loop
        
        Scanner scanner = new Scanner(System.in);
        
        int rows;
        int coulmn;
        String symbol = "";
        
        System.out.println("Enter rows: ");
        rows = scanner.nextInt();
        
        System.out.println("Enter coulmn: ");
        coulmn = scanner.nextInt();
        
        System.out.println("Enter symbol: ");
        symbol = scanner.next();
        
        for(int i=1; i<=rows; i++){
            System.out.println();
            for(int j=1;j<=coulmn;j++){
                System.out.print(symbol);
        
            }
        }
                
        
    }
    public static void Arrays(){
        
        // arrays = used to store multiple values in a single variable
        //Have to be the SAME data type 
        /*String[] cars = {"Camaro","Tesla","Merc","BMW"};
        
        cars[0] = "Mustang";
        
        System.out.println(cars[3]);
        */
        
        //additional way to store data in a array by first creating the elements then entering the values of the elements later on in the program
        
        String[] cars = new String[3];
        
        cars[0]="Camaro";
        cars[1]="Tesla";
        cars[2]="BMW";
        
        for(int i = 0;i<cars.length;i++){
            System.out.println(cars[i]);
        }
    
    }
    public static void TwoDArrays(){
    
        //2d Arrays = an array of arrays
        
        String[][] cars = new String[3][3];
        
                cars[0][0] = "Camaro";
                cars[0][1] = "BMW";
                cars[0][2] = "Aston";
                cars[1][0] = "Ferrari";
                cars[1][1] = "Merc";
                cars[1][2] = "Mclaren";
                cars[2][0] = "Red Bull";
                cars[2][1] = "Alpha";
                cars[2][2] = "Bugatti";
                
                for(int i=0;i<cars.length;i++){
                    System.out.println();
                    for(int j=0;j<cars[i].length;j++){
                        System.out.println(cars[i][j]);
                    }
                }
        /*        
        for (String[] car : cars) {
            System.out.println();
            for (String car1 : car) {
                System.out.println(car1);
            }
        }
        */      

                    
    }
    public static void Arraylists(){
        
//        ArrayList = a resizable array.
//        Elements can be added and removed  after the compilation
//        phase and store reference data types
//    

        JavaPractise obj = new JavaPractise();
        String username;
        String password;



        
    }
}
 







