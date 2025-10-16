from linked_list import Node, LinkedList

class Task:
    def __init__(self, name):
        self.name = name
        self.complete = "incomplete"

class ToDoList(LinkedList):
    def __init__(self, name):
        self.name = name        

    def add_task(self, task):
        new_task = Task(task)
        self.append(new_task)
        print(f"Task added: '{new_task.name}'")

    def complete_task(self, position):
        task = self.get_at_position(position)
        print(f"{task.complete}")

    def remove_task(self, position):
        removed_task = self.task_list.delete_at_position(position)
        print(f"{removed_task} removed")

    def view_all_tasks(self):
        print("======= TASK LIST =======")
        self.task_list.traverse()

def test_todo_list():
    """Test function to verify ToDoList functionality"""
    print("=== Testing To-Do List Implementation ===\n")
    
    # Create a new to-do list
    todo = ToDoList("School Tasks")
    
    # Test adding tasks
    print("1. Adding tasks...")
    todo.add_task("Study for math exam")
    todo.add_task("Write history essay")
    todo.add_task("Submit science project")
    todo.add_task("Read chapter 5")
    
    # Test viewing all tasks
    print("\n2. Viewing all tasks:")
    todo.view_all_tasks()
    
    # Test completing tasks
    print("\n3. Completing some tasks...")
    todo.complete_task(2)  # Complete second task
    todo.complete_task(4)  # Complete fourth task
    
    # Test viewing after completion
    print("\n4. Viewing tasks after completion:")
    todo.view_all_tasks()
    
    
    # Test removing tasks
    print("\n5. Removing a task...")
    todo.remove_task(3)  # Remove third task
    todo.view_all_tasks()
    
    # Test edge cases
    print("\n6. Testing edge cases...")
    print("Trying to complete task at invalid position:")
    result = todo.complete_task(10)  # Position that doesn't exist
    print(f"Result: {result}")
    
    print("Trying to remove task at invalid position:")
    result = todo.remove_task(0)  # Invalid position (should be 1-indexed)
    print(f"Result: {result}")
    
    print("\n=== Test completed! ===")

# Run the test
test_todo_list()