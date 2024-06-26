class Ofis():
    def __init__(self,name,surname,project_num,salary):
        self.name = name
        self.surname = surname
        self.project = project_num
        self.salary = salary
    def calculation(self):
        sum_salary = 0
        sum_salary += self.salary
        return sum_salary
    def expenses(self):
        sum_project = 0
        sum_project = sum_project + (self.project)*500
        return self.calculation() + sum_project

calisan1 = Ofis("ece","şişer",2,5000)
ccalisan2 = Ofis("çiğdem","şişer",1,15000)
print(calisan1.expenses())