"""
Class-based dict allowing tuple subscripting and sparse data.
"""
class DimensionalArrayError(Exception):
    def __init__(self,expr):
        self.expr = expr
        
class array:
    """
    create an N dimensional array
    """
    def __init__(self, *args):
        "Create an M-element list of N-element row lists."
        self._data = {}
        self._n_dimensions = args
    
    def __getitem__(self, key):
        "Returns the appropiate element for a two-element subscript tuple."
        n_key = self._validate_key(key)
        try:
            return self._data[n_key]
        except KeyError:
            return 0
        
    def __setitem__(self, key, value):
        "Sets the appropiate element for a two-element subscript tuple."
        n_key = self._validate_key(key)
        self._data[n_key] = value
        
    def _validate_key(self, key):
        """Validates a key against the array's shape, returning good tuples.
        Raises KeyError on problems."""
        n_key = key
        if len(n_key) == len(self._n_dimensions):
            for num, val in enumerate(self._n_dimensions):
                if 0 <= n_key[num] < val:
                    continue
                else:
                    raise KeyError("Subscript out of range")
            return key
        raise DimensionalArrayError("Dimensions should be equal: expected: {0}, given: {1}".format(len(self._n_dimensions), len(n_key)))
    