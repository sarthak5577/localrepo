package chatsys;

import java.util.Scanner;

class User extends Thread {

	
boolean running = true;
boolean paused = false;

User(String name) {
    super(name);
}

public void run() {

    int i = 1;

    while (running) {

        if (!paused) {
            System.out.println(getName() + " : Message " + i);
            i++;
        }

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            break;
        }
    }

    System.out.println(getName() + " stopped.");
}


}

public class MultiThreadedChat {


static User alice;
static User bob;
static User charlie;

static void startChat() {

    alice = new User("Alice");
    bob = new User("Bob");
    charlie = new User("Charlie");

    alice.start();
    bob.start();
    charlie.start();

    System.out.println("Chat Started.");
}

static void pauseChat() {

    if (alice != null) alice.paused = true;
    if (bob != null) bob.paused = true;
    if (charlie != null) charlie.paused = true;

    System.out.println("Chat Paused.");
}

static void resumeChat() {

    if (alice != null) alice.paused = false;
    if (bob != null) bob.paused = false;
    if (charlie != null) charlie.paused = false;

    System.out.println("Chat Resumed.");
}

static void stopChat() {

    if (alice != null) {
        alice.running = false;
        alice.interrupt();
    }

    if (bob != null) {
        bob.running = false;
        bob.interrupt();
    }

    if (charlie != null) {
        charlie.running = false;
        charlie.interrupt();
    }

    System.out.println("Chat Stopped.");
}

static void checkThreads() {

    System.out.println();
    System.out.println("===== THREAD STATUS =====");

    System.out.println(
        "Alice   : " +
        (alice != null && alice.isAlive() ? "Running" : "Stopped")
    );

    System.out.println(
        "Bob     : " +
        (bob != null && bob.isAlive() ? "Running" : "Stopped")
    );

    System.out.println(
        "Charlie : " +
        (charlie != null && charlie.isAlive() ? "Running" : "Stopped")
    );
}

public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int choice = 0;

    while (choice != 6) {

        System.out.println();
        System.out.println("===== CHAT MENU =====");
        System.out.println("1. Start Chat");
        System.out.println("2. Pause Chat");
        System.out.println("3. Resume Chat");
        System.out.println("4. Stop Chat");
        System.out.println("5. Check Threads");
        System.out.println("6. Exit");
        System.out.print("Enter choice: ");

        choice = sc.nextInt();

        if (choice == 1) {
            startChat();
        }
        else if (choice == 2) {
            pauseChat();
        }
        else if (choice == 3) {
            resumeChat();
        }
        else if (choice == 4) {
            stopChat();
        }
        else if (choice == 5) {
            checkThreads();
        }
        else if (choice == 6) {
            stopChat();
            System.out.println("Exiting...");
        }
        else {
            System.out.println("Invalid choice!");
        }
    }

    sc.close();
}


}
