class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound)
        self.breed = breed

    def make_sound(self):
        print(f"Dog says:{self.sound}")

class Cat(Animal):
    def __init__(self,name,sound,color):
        super().__init__(name,sound)
        self.color = color
    def make_sound(self):
        print(f"Cat says:{self.sound}") 

dog=Dog('Rover','Woof','Golden Retriever')  
dog.make_sound()

cat=Cat('Whiskers','Meow','Black')
cat.make_sound()

