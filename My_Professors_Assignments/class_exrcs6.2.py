class Animal():
    def __init__(self,age):
        self._age = age
        self._name = None

    def get_age(self):
        return self._age
    
    def get_name(self):
        return self._name
    
    def set_age(self,newage):
        self.age = newage

    def set_name(self,newname=" "):
        self.name = newname

    def __str__(self):
        return "Animal" + str(self.name) +" " + str(self.age)
    
class Cat(Animal):
    def speak(self):
        return "meow"

    def __str__(self):
        return "cat: " + str(self.name) + "," + str(self.age)
    
class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends
    
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        return "Hello"
    
    def age_diff(self,other):
        diff  = self.age - other.age
        print(abs(diff),"year difference between them.")

    def __str__(self):
        return "Person: " + str(self.name) + " is "+ str(self.age) + " years old and says " + self.speak()



my_animal = Cat(3)
my_person = Person("Ece", 19)
print(my_person)
my_animal.set_name("Pauli")
print(my_animal.get_name())
print(my_animal.get_age())
my_animal.set_name("Pasha")
print(my_animal.get_name())