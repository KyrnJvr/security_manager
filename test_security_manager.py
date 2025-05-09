import csv
import unittest
import os
from unittest.mock import patch

from security_manager import (
    SecurityTask,
    addTask, 
    viewTasks, 
    updateTask, 
    deleteTask, 
    createUserFile
)

class TestSecurityTask(unittest.TestCase):


    def setUp(self):
        # Create sample task objects for testing
        self.task1 = SecurityTask("Install Antivirus", "10/05/2025", "A", "Desktop", "Not Yet")
        self.task2 = SecurityTask("Update Password", "12/05/2025", "B", "Mobile", "In Progress")
        self.tasks = [self.task1, self.task2]

    def test_addTask(self):
        """Test the addTask function with mock user inputs"""
        # Mock input values for task creation
        mock_inputs = [
            "Install Antivirus",  # task_details
            "10/05/2025",         # due_date
            "A",                  # priority
            "Desktop",            # category
            "Not Yet"             # status
        ]
        
        # Create the expected SecurityTask object
        expected_task = SecurityTask(
            "Install Antivirus", 
            "10/05/2025", 
            "A", 
            "Desktop", 
            "Not Yet"
        )
        
        # Patch the input function to return our test inputs
        with patch('builtins.input', side_effect=mock_inputs):
            # Call the addTask function
            result = addTask()
            
            # Verify all attributes match expected values
            self.assertEqual(result.getTaskDetails(), expected_task.getTaskDetails())
            self.assertEqual(result.getDueDate(), expected_task.getDueDate())
            self.assertEqual(result.getPriority(), expected_task.getPriority())
            self.assertEqual(result.getCategory(), expected_task.getCategory())
            self.assertEqual(result.getStatus(), expected_task.getStatus())

    def test_viewTasks(self):
        """Test the viewTasks function displays tasks correctly"""
        # Capture the printed output
        with patch('sys.stdout') as mock_stdout:
            viewTasks(self.tasks)
            
            # Get the captured output
            output = mock_stdout.write.call_args_list
            
            # Convert captured output to a string for easier testing
            printed_lines = ''.join([call[0][0] for call in output])
            
            # Check header is present
            self.assertIn("Task", printed_lines)
            self.assertIn("Due Date", printed_lines)
            self.assertIn("Priority", printed_lines)
            self.assertIn("Category", printed_lines)
            self.assertIn("Status", printed_lines)
            
            # Check both tasks are displayed
            self.assertIn("Install Antivirus", printed_lines)
            self.assertIn("10/05/2025", printed_lines)
            self.assertIn("A", printed_lines)
            self.assertIn("Desktop", printed_lines)
            self.assertIn("Not Yet", printed_lines)
            
            self.assertIn("Update Password", printed_lines)
            self.assertIn("12/05/2025", printed_lines)
            self.assertIn("B", printed_lines)
            self.assertIn("Mobile", printed_lines)
            self.assertIn("In Progress", printed_lines)
            
            # Check formatting - ensure there's a separator line
            self.assertIn("-"*90, printed_lines)

    def test_updateTask(self):
        """Test the updateTask function with various update options"""
        test_task = SecurityTask("Test Task", "01/05/2025", "B", "Desktop", "Not Yet")
        
        # Test update task details (option 'a')
        with patch('builtins.input', return_value="New Task Name"), \
             patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'a')
            
            self.assertTrue(result)
            self.assertEqual(test_task.getTaskDetails(), "New Task Name")
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Task details updated successfully", printed_output)
        
        # Test update due date (option 'b')
        with patch('builtins.input', side_effect=["invalid", "15/06/2025"]), \
             patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'b')
            
            self.assertTrue(result)
            self.assertEqual(test_task.getDueDate(), "15/06/2025")
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Due date updated successfully", printed_output)
        
        # Test update priority (option 'c')
        with patch('builtins.input', side_effect=["D", "C"]), \
             patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'c')
            
            self.assertTrue(result)
            self.assertEqual(test_task.getPriority(), "C")
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Priority updated successfully", printed_output)
            self.assertIn("Invalid priority", printed_output)  # Check error message for invalid input
        
        # Test update category (option 'd')
        with patch('builtins.input', side_effect=["Laptop", "Mobile"]), \
             patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'd')
            
            self.assertTrue(result)
            self.assertEqual(test_task.getCategory(), "Mobile")
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Category updated successfully", printed_output)
            self.assertIn("Invalid category", printed_output)  # Check error message for invalid input
        
        # Test update status (option 'e')
        with patch('builtins.input', side_effect=["Pending", "Completed"]), \
             patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'e')
            
            self.assertTrue(result)
            self.assertEqual(test_task.getStatus(), "Completed")
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Status updated successfully", printed_output)
            self.assertIn("Invalid status", printed_output)  # Check error message for invalid input
        
        # Test exit update (option 'f')
        with patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'f')
            
            self.assertFalse(result)
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Cancelling update", printed_output)
        
        # Test invalid update option
        with patch('sys.stdout') as mock_stdout:
            result = updateTask(test_task, 'z')
            
            self.assertFalse(result)

    def test_deleteTask(self):
        """Test the deleteTask function for deleting tasks with confirmation"""
        # Create a copy of tasks list to avoid modifying the original
        test_tasks = self.tasks.copy()
        original_length = len(test_tasks)
        
        # Test invalid task index (out of range)
        with patch('sys.stdout') as mock_stdout:
            result = deleteTask(test_tasks, 0)  # Index 0 is invalid (should be 1-based)
            
            self.assertFalse(result)
            self.assertEqual(len(test_tasks), original_length)  # List unchanged
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Please enter a valid number", printed_output)
        
        # Test deletion with confirmation (yes)
        with patch('builtins.input', return_value="y"), \
            patch('sys.stdout') as mock_stdout:
            
            task_to_delete = test_tasks[0].getTaskDetails()
            result = deleteTask(test_tasks, 1)  # Delete the first task
            
            self.assertTrue(result)
            self.assertEqual(len(test_tasks), original_length - 1)  # One item removed
            self.assertNotEqual(test_tasks[0].getTaskDetails() if test_tasks else None, task_to_delete)  # First item changed
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("has been deleted", printed_output)
        
        # Test deletion cancelled (no)
        remaining_tasks = len(test_tasks)
        with patch('builtins.input', return_value="n"), \
            patch('sys.stdout') as mock_stdout:
            
            result = deleteTask(test_tasks, 1)  # Try to delete the first task
            
            self.assertFalse(result)
            self.assertEqual(len(test_tasks), remaining_tasks)  # List unchanged
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Deletion cancelled", printed_output)
        
        # Test invalid confirmation input then confirmation
        with patch('builtins.input', side_effect=["x", "y"]), \
            patch('sys.stdout') as mock_stdout:
            
            task_to_delete = test_tasks[0].getTaskDetails()
            result = deleteTask(test_tasks, 1)  # Delete the first task after invalid input
            
            self.assertTrue(result)
            self.assertEqual(len(test_tasks), remaining_tasks - 1)  # One item removed
            printed_output = ''.join([call[0][0] for call in mock_stdout.write.call_args_list])
            self.assertIn("Invalid input", printed_output)
            self.assertIn("has been deleted", printed_output)

    def test_createUserFile(self):
        """Test the createUserFile function for creating new CSV files with headers"""
        test_filename = "test_create_user_file.csv"
        
        try:
            # Call the function
            result = createUserFile(test_filename)
            
            # Check return value
            self.assertEqual(result, [])  # Should return empty list
            
            # Verify file exists
            self.assertTrue(os.path.exists(test_filename))
            
            # Check file contents - should have headers only
            with open(test_filename, 'r', newline='') as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                self.assertEqual(headers, ["Task Details", "Due_Date", "Priority", "Category", "Status"])
                
                # Make sure there are no other rows (empty file except headers)
                self.assertEqual(list(reader), [])
                
        finally:
            # Clean up - remove test file
            if os.path.exists(test_filename):
                os.remove(test_filename)


if __name__ == '__main__':
    unittest.main()
