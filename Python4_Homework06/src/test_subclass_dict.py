from subclass_dict import Dictionary
import unittest

class TestDictionary(unittest.TestCase):
    def test__error(self):
        d = Dictionary()
        self.assertRaises(TypeError, d["a"])
        d2 = Dictionary("b")
        self.assertRaises(TypeError, d2["a"])
    
    def test_return_key(self):
        d = Dictionary()
        actual = d["a"]
        expected = "DefKey"
        self.assertEqual(expected, actual)
        d2 = Dictionary("b")
        actual = d2["a"]
        expected = "b"
        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()