''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
'''

print("===== What is class ====")
# CLASSlar object yasash uchun xizmat qiladigan shablon
# class - blueprint for object creation!
# structure > state, constructure, method


class Person():
    # state
    message = "class state property"

    # constructure
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):  # classlarni methodi deyiladi function emas
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("Class: static method property executed")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state
name = person1.name
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("===== ordinary vs static properties ====")
# ORDINARY state & methods lar object bilan birga yashaydiganlari
# STATIC state & methods tugridan tugri classdan keladiganlari

# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
