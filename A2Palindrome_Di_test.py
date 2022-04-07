
import unittest
from A2Palindrome_DI import tellifpalindrome

class A2PalindromeDI(unittest.TestCase):
    def tellifpalindrome(self):
        self.assertEqual(tellifpalindrome("reviver"), True)
        self.assertEqual(tellifpalindrome("elephant"), False)

    def tellifpalindrome(self):
        self.assertTrue(tellifpalindrome("reviver"))
        self.assertTrue(tellifpalindrome("elephant"))


if __name__ == '__main__':
    unittest.main()
