import random
class Animal():
    def __init__(self,age):
        self._age = age
        self._name = None

    def get_age(self):
        return self._age
    
    def get_name(self):
        return self._name
    
    def set_age(self,newage):
        self._age = newage

    def set_name(self,newname=" "):
        self._name = newname

    def __str__(self):
        return "Animal" + str(self._name) +" " + str(self._age)
    
class Cat(Animal):
    def speak(self):
        return "meow"

    def __str__(self):
        return "cat: " + str(self._name) + "," + str(self._age)
    
class Person(Animal):

    friends = []

    def get_friends(self):
        return self.friends
    
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        return "Hello"
    
    def age_diff(self,other):
        diff  = self._age - other._age
        print(abs(diff),"year difference between them.")

    def __str__(self):
        return "Person: " + str(self._name) + " is "+ str(self._age) + " years old and says " + self.speak()

class Student(Person):
    def __init__(self, age):
        Person.__init__(self, age)
        self.name = self.get_name()

    
    def speak(self):
        r = random.random()
        if r < 0.25:
            return ("I have homeworks.")
        elif 0.25 <= r <= 0.75:
            return ("I need to sleep.")
        else:
            return ("I am watching serie.")

    def __str__(self):
        return "Student: " + str(self._name)+ " is " + str(self._age) + " years old and says " + "\"" + self.speak() + "\""

my_animal = Cat(3)
my_person = Person(19)
my_person2 = Person(22)
my_person2.set_name("Dogu")
my_person.set_name("Ece")
my_person.add_friend(my_person2.get_name())
print(my_person.get_friends())
print(my_person)
mystudent = Student(19)
mystudent.set_name("Ece")
mystudent2 = Student(22)
mystudent2.set_name("Dogu")
print(mystudent)
print(mystudent2)