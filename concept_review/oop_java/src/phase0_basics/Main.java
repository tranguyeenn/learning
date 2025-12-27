package phase0_basics;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] names = {"Trang", "Alex", "Jamie", "Sam"};
        int[] scores = {95, 72, 88, 40};

        Scanner scanner = new Scanner(System.in);
        int choice;

        while (true) {

            do {
                System.out.println("\nMenu:");
                System.out.println("1. Show all students");
                System.out.println("2. Show passing students");
                System.out.println("3. Show class statistics");
                System.out.println("4. Exit");
                System.out.print("Choose an option: ");

                choice = scanner.nextInt();

                if (choice < 1 || choice > 4) {
                    System.out.println("Invalid choice. Try again.");
                }

            } while (choice < 1 || choice > 4);

            switch (choice) {

                case 1:
                    for (int i = 0; i < scores.length; i++) {
                        if (scores[i] >= 50) {
                            System.out.println(names[i] + " passed with " + scores[i]);
                        } else {
                            System.out.println(names[i] + " failed with " + scores[i]);
                        }
                    }
                    break;

                case 2:
                    System.out.println("Passing students:");
                    for (int i = 0; i < scores.length; i++) {
                        if (scores[i] < 50) {
                            continue;
                        }
                        System.out.println(names[i] + " passed with " + scores[i]);
                    }
                    break;

                case 3:
                    int sum = 0;
                    int maxScore = scores[0];
                    int minScore = scores[0];

                    for (int score : scores) {
                        sum += score;
                        maxScore = Math.max(maxScore, score);
                        minScore = Math.min(minScore, score);
                    }

                    double average = (double) sum / scores.length;

                    System.out.println("Class average: " + Math.round(average));
                    System.out.println("Highest score: " + maxScore);
                    System.out.println("Lowest score: " + minScore);
                    break;

                case 4:
                    System.out.println("Program ended. Data processed successfully.");
                    return;
            }
        }
    }
}
