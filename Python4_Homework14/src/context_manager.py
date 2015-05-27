"""
context_manager.py: suppress ValueError exceptions
"""
class ctx_mgr:
    def __enter__(self):
        print("enter called")
        cm = object()
        return cm
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if exc_type != ValueError:
                print("An exception occurred")
            else:
                self.raising = False
                print("exit called")
                return not self.raising
            
if __name__ == "__main__":
    with ctx_mgr() as cm:
        int("x")
    print("*"*10)
    with ctx_mgr() as cm:
        3/1
    print("*"*10)
    with ctx_mgr() as cm:
        3/0
        
            