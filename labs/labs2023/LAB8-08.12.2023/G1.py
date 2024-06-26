class Person():
    def __init__(self,first_name,last_name,age,department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
class Student(Person):
    courses = ["Com101","Com201","Com301"]
    new_courses = []
    def __init__(self, first_name, last_name, age, department,id):
        super().__init__(first_name, last_name, age, department)
        self.id = id
    def get_student_id(self):
        return self.id
    def control_and_add_course(self,course):
        if course in self.courses:
            return "{} already in the predefined_courses.".format(course)
        else:
            self.new_courses.append(course)
            return "{} added to the courses.".format(course)
    def remove_course(self,course):
        if course in self.new_courses:
            self.new_courses.remove(course)
            return "{} removed from the course.".format(course)
        else:
            return "{} is not in the courses.".format(course)
    
    def get_courses(self):
        return self.new_courses
    
    def __str__(self):
        return "Student: {} {}, Age: {}, Department: {} Student ID: {}, Courses: {}".format(self.first_name,self.last_name,self.age,self.department,self.id,",".join(self.new_courses))
class Graduate(Person):
    def __init__(self, first_name, last_name, age, department,graduationYear,gpa):
        super().__init__(first_name, last_name, age, department)
        self.gY = graduationYear
        self.gpa = gpa
    def get_gradution_year(self):
        return self.gY
    def get_gradution_gpa(self):
        return self.gpa
    def __str__(self):
        return "Graduate: {} {}, Age: {}, Department: {} Graduation Year: {}, Graduation GPA: {}".format(self.first_name,self.last_name,self.age,self.department,self.gY,self.gpa)
    
class Instructor(Person):
    def __init__(self, first_name, last_name, age, department,branch):
        super().__init__(first_name, last_name, age, department)
        self.branch = branch

    def get_main_branch(self):
        return self.branch
    
    def __str__(self):
        return "Instructor: {} {}, Age: {}, Department: {} , Main Branch: {}".format(self.first_name,self.last_name,self.age,self.department,self.branch)


student1 = Student("Ahmet","Yilmaz",20,"Computer Engineering",12345)
inst1 = Instructor("Ayse","Demir",35,"Computer Engineering","Computer Science")
grdt1 = Graduate("Cem","Kara",25,"Computer Engineering",2020,3.5)
print(student1.control_and_add_course("Math101"))
print(student1.control_and_add_course("Physics101"))
print(student1.control_and_add_course("Com101"))
print(student1.remove_course("Physics101"))
print(student1.control_and_add_course("Comp102"))
print(student1)
print(inst1)
print(grdt1)