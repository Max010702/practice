''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument 
(3) Keyword & default arguments
(4) Scope
'''

print("==== DEFINE vs CALL ====")
# build in functions > print() type()
#  Function - reunable block of code
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - build - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute - argument
result1 = greet('Max')
print("result", result1)


result2 = greeting('Justin')
print("result2", result2)
