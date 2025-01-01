import 'dart:io';
import 'Maintanance.dart';

void main() {
  // Instantiate the Maintanance class
  var maintanance = Maintanance();

  print('\t\t\tTO-DO List');
  while (true) {
    // Display the menu
    print("\n1. ADD A TASK");
    print("2. COMPLETE A TASK");
    print("3. DELETE A TASK");
    print("4. LIST TASKS");
    print("5. EXIT");
    stdout.write('ENTER YOUR CHOICE: ');

    // Parse user choice
    var choice = int.tryParse(stdin.readLineSync() ?? '');

    if (choice == null) {
      print("Invalid input. Please enter a number between 1 and 5.");
      continue;
    }

    switch (choice) {
      case 1: // Add a task
        stdout.write('Enter a task: ');
        String title = stdin.readLineSync() ?? '';
        if (title.trim().isEmpty) {
          print("Task title cannot be empty.");
        } else {
          maintanance.addTask(title);
        }
        break;

      case 2: // Complete a task
        if (maintanance.task.isEmpty) {
          print("No tasks available to complete.");
          break;
        }
        stdout.write('Enter the index of the task to mark as completed: ');
        int? index = int.tryParse(stdin.readLineSync() ?? '');
        if (index != null) {
          maintanance.completeTask(index - 1); 
        } else {
          print("Invalid input.");
        }
        break;

      case 3: // Delete a task
        if (maintanance.task.isEmpty) {
          print("No tasks available to delete.");
          break;
        }
        stdout.write('Enter the index of the task to delete: ');
        int? index = int.tryParse(stdin.readLineSync() ?? '');
        if (index != null) {
          maintanance.deleteTask(index - 1);
        } else {
          print("Invalid input.");
        }
        break;

      case 4: // List all tasks
        maintanance.listTask();
        break;

      case 5: // Exit
        print("EXITING FROM THE PROGRAM! THANK YOU FOR USING THIS APP");
        exit(0);

      default: // Invalid choice
        print("Invalid choice. Please enter a number between 1 and 5.");
        break;
    }
  }
}
