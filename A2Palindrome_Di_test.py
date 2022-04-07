import unittest
from A2Palindrome_DI import tellifpalindrome


class TestA2PalindromeDI(unittest.TestCase):
    def testtellifpalindrome_1(self):
        self.assertEqual(tellifpalindrome("reviver"), True)
        self.assertEqual(tellifpalindrome("elephant"), False)

    def test_tellifpalindrome_2(self):
        self.assertTrue(tellifpalindrome("reviver"))
        self.assertFalse(tellifpalindrome("elephant"))


if __name__ == '__main__':
    unittest.main()
