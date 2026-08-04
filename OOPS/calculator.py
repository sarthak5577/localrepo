# package first;
# import java.util.*;

# public class first {
#     public static void main(String args[]) {

#         Scanner sc = new Scanner(System.in);
#         int choice;

#         do {
#             System.out.println("\n===== MY CALCULATOR  =====");
#             System.out.println("1. Addition (+)");
#             System.out.println("2. Subtraction (-)");
#             System.out.println("3. Multiplication (*)");
#             System.out.println("4. Division (/)");
#             System.out.println("5. Modulus (%)");
#             System.out.println("6. Exit");
#             System.out.print("Enter your choice: ");

#             choice = sc.nextInt();

#             if (choice >= 1 && choice <= 5) {

#                 System.out.print("Enter First Number: ");
#                 double num1 = sc.nextDouble();

#                 System.out.print("Enter Second Number: ");
#                 double num2 = sc.nextDouble();

#                 switch (choice) {

#                     case 1:
#                         System.out.println("Addition = " + (num1 + num2));
#                         break;

#                     case 2:
#                         System.out.println("Subtraction = " + (num1 - num2));
#                         break;

#                     case 3:
#                         System.out.println("Multiplication = " + (num1 * num2));
#                         break;

#                     case 4:
#                         if (num2 == 0) {
#                             System.out.println("Division not possible. Second number is zero.");
#                         } else {
#                             System.out.println("Division = " + (num1 / num2));
#                         }
#                         break;

#                     case 5:
#                         if (num2 == 0) {
#                             System.out.println("Modulus not possible. Second number is zero.");
#                         } else {
#                             System.out.println("Modulus = " + (num1 % num2));
#                         }
#                         break;
#                 }

#             } else if (choice == 6) {
#                 System.out.println("Thank you for using Calculator!");
#             } else {
#                 System.out.println("Invalid Choice! Please try again.");
#             }

#         } while (choice != 6);

#         sc.close();
#     }
# }