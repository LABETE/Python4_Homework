""" 
Program for optimization. Python 4, Lesson 5. 

Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 
from math import log 
from timeit import Timer 
from functools import reduce
from itertools import accumulate

def groffle_slow(mass, density): 
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)

    return total

def groffle_slow2(mass, density): 
    masslog = log(mass * density) 
    val_added = 1.0
    lst = map(val_added.__add__, range(10000))
    lst = map(masslog.__truediv__, lst)
    
    return sum(lst)

def groffle_slow3(mass, density): 
    lst = range(10000)
    masslog = log(mass * density) 
    #for i in lst: 
    lst = [masslog/(i+1) for i in lst]

    return sum(lst)

mass = 2.5 
density = 12.0 

timer = Timer("total = groffle_slow(mass, density)", 
 "from __main__ import groffle_slow, mass, density") 
print("time:", timer.timeit(number=1000)) 
timer = Timer("total = groffle_slow2(mass, density)", 
 "from __main__ import groffle_slow2, mass, density") 
print("time2:", timer.timeit(number=1000)) 
timer = Timer("total = groffle_slow3(mass, density)", 
 "from __main__ import groffle_slow3, mass, density") 
print("time3:", timer.timeit(number=1000)) 

