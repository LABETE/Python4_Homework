import os
import threading

class Thread(threading.Thread):
    def __init__(self, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
    def run(self):
        print(self.name, "finished", "with directory:", os.getcwd())

class ThreadChdir(threading.Thread):
    def __init__(self, path, *args, **kw):
        threading.Thread.__init__(self, *args, **kw)
        self.path = path
    def run(self):
        os.chdir(self.path)
        print(self.name, "changed directory")
path = "V:\workspace\Python4_Homework10\src"

t1 = Thread()
tchdir = ThreadChdir(path)
t2 = Thread()
print("Threads created")
t1.start()
tchdir.start()
t2.start()
print("Threads started")