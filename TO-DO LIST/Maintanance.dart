import 'Task.dart';

class Maintanance {
  // Task list to store all tasks
  List<Task> task = [];

  // Add a new task
  void addTask(String title) {
    task.add(Task(title));
    print('Task added successfully!');
  }

  // Mark a task as complete
  void completeTask(int index) {
    if (index >= 0 && index < task.length) {
      task[index].isComplete = true;
      print('Task has been marked as completed.');
    } else {
      print('Invalid task index.');
    }
  }

  // Delete a task
  void deleteTask(int index) {
    if (index >= 0 && index < task.length) {
      task.removeAt(index);
      print('Task deleted.');
    } else {
      print('Invalid task index.');
    }
  }

  // List all tasks
  void listTask() {
    if (task.isEmpty) {
      print('No tasks available.');
    } else {
      for (var i = 0; i < task.length; i++) {
        print('${i + 1}. ${task[i].title} - ${task[i].isComplete ? "Done" : "Pending"}');
      }
    }
  }
}
