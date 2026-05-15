''' List
    (1) Working with lists 
    (2) List methods
    (3) Lambda function
    (4) enumarate, map and filter
'''

print("==== Working with lists ====")
# JAVA/PHP/NodeJS array => Python list, array

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "john", "michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello world!")
print(f"the letters: {result} and size: {len(result)}")

print("-----")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("==== List methods ====")
# methods > append() insert() pop() remove() clear() sort()   immutable.      index(). mutable

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters {letters}")


print("-----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:5]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)


if "cat" in animals:
    print("Index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("-----")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable > sorted function & index method
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("==== Lambda function ====")
# lambda is small anonymous function:
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)
