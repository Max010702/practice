''' OBJECTS 
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math  # package/module
from math import ceil, asin  # packageni ichidagi method
print("==== What is Object ====")
# OBJECTLAR - uzining bir qator state va method propertylarga ega bulgan dada type
# An object has state and method properties
# Everything is object in Pyton (Xamma narsa object)!

'''Inson object misolida: 
    uning statelari: uning irqi, ismi, yoshi, familiyasi ...
    methodlari: salomlashihshi, yurishi, ishlashi...
'''

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstarction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # CALL.   - maqsadli method
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)
