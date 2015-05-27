
class Dictionary(dict):
    def __init__(self, key="DefKey"):
        dict.__init__(self)
        self.key = key
    def __getitem__(self, key):
        try:
            dict.__getitem__(key)
        except TypeError:
            return self.key
        
if __name__ == "__main__":
    d = Dictionary()
    d["a"] = 1
    d["b"] = 2
    print(d["c"])