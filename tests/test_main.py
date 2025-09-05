import unittest
from unittest.mock import patch
from io import StringIO
from src.cripchat.main import start_cripchat # Import the function to be tested

class TestMain(unittest.TestCase):
    
    # A test method must start with the word "test_"
    def test_start_cripchat_prints_welcome_message(self):
        """
        Tests if the start_cripchat function prints the correct welcome message to the console.
        """
        
        # This context manager temporarily captures anything sent to stdout (the print function)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            start_cripchat() # Call the function
            
            # Get the string that was "printed" and remove any leading/trailing whitespace
            printed_output = fake_out.getvalue().strip()
            
            # Define the exact message we expect to see
            expected_message = "Welcome to Cripchat. The backend is running!🔥"
            
            # Assert that the captured output is equal to the expected message
            # If they are not equal, the test will fail.
            self.assertEqual(printed_output, expected_message)

# This allows running the test file directly, though it's not common
if __name__ == '__main__':
    unittest.main()