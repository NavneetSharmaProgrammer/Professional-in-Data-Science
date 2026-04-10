class Animal:
    location = "Africa"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now...")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak()
        print("Woof! Woof!")

d = Dog("Jacky")
d.speak()  # Output: Woof! Woof!
print(d.location)  # Output: Africa