import random
class Student():
    year = "2023"
    counter = 0
    def __init__(self,name,surname,age):  
        Student.counter += 1
        self.name = name
        self.surname = surname
        self.age = age
        self.id = self.student_id()

    def student_id(self):
        born_year = str(int(self.year) - int(self.age))
        bornyear2 =  str(born_year[0])
        year2 = str(self.year[-2]) + str(self.year[-1])
        if self.counter < 10:
            addnum = self.counter
            addnum2 = random.randint(999,10000)
        elif self.counter >= 10 and self.counter < 100:
            addnum = self.counter
            addnum2 = random.randint(99,1000)
            
        elif self.counter >= 100:
            addnum = self.counter
            addnum2 = random.randint(9,100)
        return str(year2) + str(bornyear2) + str(addnum) + str(addnum2)

    def get_id(self):
        return str(self.id)
    
    

std1 = Student("Ece", "Şişer","19")
print(std1.get_id())
std2 = Student("Doğukan","Filiz","22")
print(std2.get_id())

