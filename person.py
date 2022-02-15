from dog import Dog

class Person:
    name = str
    age = int
    pet =  Dog

    def __init__(self, name:str, age:int, pet):
        self.pet = pet
        self.name = name
        self.age = age


    def walk_dog(self):
        return f'{self.name} is walking {self.pet}'

    def walk_dog(self):
        return f'{self.name} is teaching {self.pet} a new trick'

        person1 = Person("Luke", 90, Dog("Mike",5,["paw,","sit","run"]))
        print(person1)


