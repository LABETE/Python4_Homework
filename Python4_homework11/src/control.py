"""
control.py: Creates queues, starts output and worker threads,
            and pushes inputs into the input queue.
"""
from queue import Queue
from output import OutThread
from worker import WorkerThread
from random import randint
from timeit import timeit

def control():
    WORKERS = 10

    inq = Queue(maxsize=int(WORKERS*1.5))
    outq = Queue(maxsize=int(WORKERS*1.5))

    ot = OutThread(WORKERS, outq)
    ot.start()

    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = [chr(randint(97, 122)) for _ in range(1000)]
    for work in enumerate(instring):
        inq.put(work)
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control thread terminating")
    
if __name__ == "__main__":
    print(timeit("control()", "from __main__ import control", number=1))