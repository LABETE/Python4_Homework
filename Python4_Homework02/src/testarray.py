"""
Test list-of-list based array implementations using tuple subscripting.
"""
import unittest
import arr

class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], 0)
    
    def test_identity(self):
        for N in range(4):
            a = arr.array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[i, j, k], i==j==k)
    
    def _index(self, a, r, c, d):
        return a[r, c, d]
    
    def _index_error(self, a, r, c):
        return a[r, c]
    
    def _index_errror2(self, a, r, c, d, e):
        return a[r, c, d, e]
    
    def test_key_validity(self):
        a = arr.array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)
        self.assertRaises(KeyError, self._index, a, 1, 1, 10)
        self.assertRaises(arr.DimensionalArrayError, self._index_error, a, 1, 1)
        self.assertRaises(arr.DimensionalArrayError, self._index_errror2, a, 1, 1, 1, 1)
        

if __name__ == "__main__":
    unittest.main()