'''CLASS deep diving 
    (1) ENCAPSULATION
    (2) INHERITENCE <
    (3) POLIMORHISM <
'''

print("==== ENCAPSULATION ====")
# PARENT > CHILD
# Parent can only provides public & protected properties(state + method) to children


class Animal:  # Parent
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
