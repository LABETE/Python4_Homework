"""
control.py: Creates queues, starts output and worker processes,
            and pushes inputs into the input queue.
"""
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
from random import randint

if __name__ == "__main__":
    WORKERS = 10
    
    inq = JoinableQueue(maxsize=int(WORKERS*1.5))
    outq = JoinableQueue(maxsize=int(WORKERS*1.5))
    
    ot = OutThread(WORKERS, outq)
    ot.start()
    
    for i in range(WORKERS):
        w = WorkerThread(inq, outq)
        w.start()
    instring = [chr(randint(97, 122)) for _ in range(1000)]
    # feed the process pool with work units
    for work in enumerate(instring):
        inq.put(work)
    # terminate process pool
    for i in range(WORKERS):
        inq.put(None)
    inq.join()
    print("Control process terminating")