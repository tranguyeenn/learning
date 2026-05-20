package app;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the first number: ");
        double num1 = input.nextDouble();
        System.out.println("Enter the second number: ");
        double num2 = input.nextDouble();

        System.out.println("Enter the operator (+, -, *, /): ");
        char operator = input.next().charAt(0);
        double result;

        if (operator == '+') {
            result = num1 + num2;
            System.out.println("The result is: " + result);
        } else if (operator == '-') {
            result = num1 - num2;
            System.out.println("The result is: " + result);
        } else if (operator == '*') {
            result = num1 * num2;
            System.out.println("The result is: " + result);
        } else if (operator == '/') {
            if (num2 != 0) {
                result = num1 / num2;
                System.out.println("The result is: " + result);
            } else {
                System.out.println("Error: Division by zero is not allowed.");
            }
        } else {
            System.out.println("Invalid operator. Please use +, -, *, or /.");
        }

        input.close();
    }
}
