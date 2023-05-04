import unittest
from lesson1.task1.task import palindrome_checker


class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome_checker("racecar"), "racecar is a palindrome!")
        self.assertEqual(palindrome_checker("A man, a plan, a canal, Panama!"), "amanaplanacanalpanama is a palindrome!")
        self.assertEqual(palindrome_checker("Was it a car or a cat I saw?"), "wasitacaroracatisaw is a palindrome!")

    def test_not_palindrome(self):
        self.assertEqual(palindrome_checker("hello world"), "helloworld is not a palindrome.")
        self.assertEqual(palindrome_checker("Python"), "python is not a palindrome.")
        self.assertEqual(palindrome_checker("This is not a palindrome"), "thisisnotapalindrome is not a palindrome.")

    def test_empty_string(self):
        self.assertEqual(palindrome_checker(""), " is a palindrome!")
