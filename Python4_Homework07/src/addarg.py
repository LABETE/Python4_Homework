def addarg(val):
    """Take a value in the decorator"""
    def decorator(f):
        """Decorates a function"""
        def wrapper(*args, **kwargs):
            """Return a tuple with the value added in the decorator + the args"""
            return f(val, *args, **kwargs)
        return wrapper
    return decorator

@addarg(1)
def prargs(*args):
    return args

