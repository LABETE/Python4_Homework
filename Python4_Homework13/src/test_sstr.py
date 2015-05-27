from sstr import sstr
import unittest

class Testsstr(unittest.TestCase):
    def test_sstr(self):
        s1 = sstr("abcde")
        actual = s1 << 0
        expected = "abcde"
        self.assertEqual(actual, expected)
        actual = s1 >> 0
        self.assertEqual(actual, expected)
        actual = s1 >> 5
        self.assertEqual(actual, expected)
        actual = s1 << 2
        expected = "cdeab"
        self.assertEqual(actual, expected)
        actual = s1 >> 2
        expected = "deabc"
        self.assertEqual(actual, expected)
        actual = (s1 >> 5) << 5 == "abcde"
        expected = True
        self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()