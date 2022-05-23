import unittest

from S_HW3 import generate_phrase


class TestS_HW3(unittest.TestCase):
    def testgenerate_phrase_1(self):
        self.assertEqual(generate_phrase("reeedg", "degree"), True)
        self.assertEqual(generate_phrase("metleto", "omelette"),False)

    def testgenerate_phrase_2(self):
         self.assertTrue(generate_phrase("eleeodpvr", "Developer"))
         self.assertFalse(generate_phrase("seci!", "science!"))

if __name__ == '__main__':
    unittest.main()