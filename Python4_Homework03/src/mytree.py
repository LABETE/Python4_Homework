class Tree:
    def __init__(self, key, data):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.data = data
        self.left = self.right = None
    def insert(self, key, data):
        "Insert a new element into the tree in the correct position."
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value")
    
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n, v in self.left.walk():
                yield n, v
        yield self.key, self.data
        if self.right:
            for n, v in self.right.walk():
                yield n, v
                
    def find(self, key):
        
        if key == self.key:
            return self.data
        elif key < self.key:
            left_right_error = "left"
            if self.left:
                for n, data in self.left.walk():
                    if n == key:
                        return data
        elif key > self.key:
            left_right_error = "right"
            if self.right:
                for n, data in self.right.walk():
                    if n == key:
                        return data
            #raise KeyError("test")
        raise KeyError("Tree object has no {0} attribute {1}".format(left_right_error, key))
        
if __name__ == '__main__':
    t = Tree("D", 1)
    for c, v in [("B",2),("J",3),("Q",4),("K",5),("F",6),("A",7),("C",8)]:
        t.insert(c,v)
    
    print(list(t.walk()))
    for c in "DAQ":
        try: 
            print(t.find(c))
        except KeyError:
            print("Tree object was not found")