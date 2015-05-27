class sstr(str):
    def __init__(self, string):
        super().__init__()
        self.string = string
    def __lshift__(self, num):
        result = self.string[num:] + self.string[:num]
        return sstr(result)
    def __rshift__(self, num):
        if num == 0:
            result = self.string
        else:
            result = self.string[num+1:] + self.string[:num+1]
        return sstr(result)
    