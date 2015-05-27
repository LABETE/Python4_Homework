"""
composable.py: defines a composable function class.
"""
import types
class Composable:
    def __init__(self, f):
        "Store reference to proxied function."
        self.func = f
        
    def __call__(self, *args, **kwargs):
        "Proxy the function, passing all arguments through."
        return self.func(*args, **kwargs)
    
    def __mul__(self, other):
        "Return the composition of the proxied and another function."
        if type(other) is Composable:
            def anon(x):
                return self.func(other.func(x))
            return Composable(anon)
        elif type(other) is types.FunctionType:
            def anon(x):
                return self.func(other(x))
            return Composable(anon)
        raise TypeError("Illegal operands for multiplications")
    
    def __pow__(self, val):
        """Return the composition of the proxied*proxied the number of times inserted.
            val should be integer and positive."""
        if not isinstance(val, int):
            raise TypeError("value should be integer")
        if not val > 0:
            raise ValueError("value should be positive")
        me = self
        for _ in range(1, val):
            me *= self
        return me
        """try:
            if val > 0:
                def anon(x):
                    for num in range(val):
                        x = self.func(x)
                    return x   
                return Composable(anon)
            else:
                raise ValueError("value should be positive")
        except TypeError: 
            raise TypeError("value should be integer")"""
        
        
    def __repr__(self):
        return "<Composable function {0} at 0x{1:X}>".format(
                            self.func.__name__, id(self))