'''CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE <
    (3) POLIMORHISM <
'''

print("==== ENCAPSULATION ====")
# PARENT > CHILD
# Parent can only provides public & protected properties(state + method) to children


class Animal:  # Parent.    class Animal(object):
    # state
    description = "This class is parent for animals"

    # constructor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
fish.make_voice()

print("------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)


print("==== POLIMORHISM ====")

dog.make_voice()
fish.make_voice()


print("------")
#  fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
