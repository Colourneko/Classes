
class Dog:
    pname = str
    age = int
    tricks = []

    def __init__(self, pname:str , age:int, tricks:list):
        self.pname = pname
        self.age = age
        self.tricks = tricks


    def bark(self):
        return f'{self.pname} is barking '
    def sit(self):
        return f'{self.pname} is sitting '

    dog1 = Dog("Mike",5,[])

    print(dog1.name.sit)
