import mmap
from timeit import timeit
import sys
import os
import io

FILENAME = "ten_mb_file_map"
FILESIZE = 10000000
FILEPATH = "v:/workspace/Python4_Homework15/src/ten_mb_file.bak"

def map_file(chunk):
    chunk
    with open(FILENAME, "a+") as f:
        mapf = mmap.mmap(f.fileno(), FILESIZE)
        pos = 0
        chunk_size = len(str(chunk))
        chunk = chunk_size * b'x'
        for _ in range(FILESIZE // chunk_size):
            mapf[pos:pos + chunk_size] = chunk
            pos += chunk_size
        mapf.close()
    os.unlink(FILENAME)

def create_file(chunk):
    chunk_size = len(str(chunk))
    chunk = chunk_size * b'x'
    with open(FILEPATH, "wb") as f:
        for _ in range(FILESIZE // chunk_size):
            f.write(chunk)

if __name__ == "__main__":
    for chunk in [1000, 10000, 10000, 1000000]:
        print("Create_map:")
        print(timeit("map_file("+str(chunk)+")", "from __main__ import map_file", number=1))
        print("create_file:")
        print(timeit("create_file("+str(chunk)+")", "from __main__ import create_file", number=1))


        