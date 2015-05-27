from timeit import timeit
from random import random
print("list:")
print(timeit("list(random() for x in range(1000000))", "from __main__ import random", number=1))
print("list comprehension:")
print(timeit("[random() for x in range(1000000)]", "from __main__ import random", number=1))