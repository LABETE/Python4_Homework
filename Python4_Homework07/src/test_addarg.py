from addarg import addarg, prargs
import unittest

@addarg("tiger ")
def concat(*strings, **kwargs):
    output = ""
    for element in strings:
        output += element
    if "uppercase" in kwargs:
        if kwargs["uppercase"]:  # uppercase = True passed as keyword argument
            output = output.upper()
    return output


class TestAddarg(unittest.TestCase):
    def test_addarg(self):
        actual = prargs(2,3)
        expected = (1,2,3)
        self.assertEqual(actual, expected)
        actual = prargs("child")
        expected = (1, 'child')
        self.assertEqual(actual, expected)
    
    def test_sumall(self):
        @addarg(10)  # make 10 the first argument
        def sumall(*seq):
            return sum(seq)  # add em up

        self.assertEqual(sumall(1,2,3), 16, "Not the right sum 10 + 1 + 2 + 3")
    
    def test_concat(self):
        observed = concat("tiger ", "burning ", "bright")
        expected = "tiger tiger burning bright"
        self.assertEqual(observed, expected, "Not the same")

    def test_concat2(self):
        observed = concat("tiger ", "burning ", "bright", uppercase=True)
        expected = "TIGER TIGER BURNING BRIGHT"
        self.assertEqual(observed, expected, "Not the same")

        
if __name__ == "__main__":
    unittest.main()