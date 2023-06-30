class Animal:
    def __init__(self,name,color):
        self.name = name

    def speak(self):
            raise NotImplementedError("child classes must implement")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meows"
dog=Dog("Tom","Brown")
print(dog.name)
print(dog.speak())


