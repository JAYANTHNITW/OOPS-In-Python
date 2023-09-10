

class U:
    def __init__(self, university_name):
        self.uni_name = university_name
    def show_deatils(self):
        print(f"Name of the university: {self.uni_name}")

class C(U):
    def __init__(self,course,university_name):
        super().__init__(university_name)
        self.course = course
    def show_deatils(self):
        super().show_deatils()
        print(f"Name of the course: {self.course}")

class B(U):
    def __init__(self,branch_name,university_name):
        super().__init__(university_name)
        self.branch = branch_name
    def show_deatils(self):
        super().show_deatils()
        print(f"Name of the branch: {self.branch}")

class Faculty(B):
    def __init__(self,faculty_name,branch_name,university_name):
        super().__init__(branch_name,university_name)
        self.faculty = faculty_name
    def show_deatils(self):
        super().show_deatils()
        print(f"Name of the faculty: {self.faculty}")

class Student(B,C):
    def __init__(self,student_name,branch,course,university_name):
        B.__init__(self,branch,university_name)
        C.__init__(self,course,university_name)
        # super().__init__( branch,university_name)
        # super().__init_subclass__(course,university_name)
        self.name = student_name
    # def __init_subclass__(self,student_name,course,university_name):
    #     super().__init__( course,university_name)
    #     self.name = student_name
    def show_deatils(self):
        super().show_deatils()
        print(f"Name of the student: {self.name}")
        #return super().show_deatils()
    
# student1 = Student("jayanth")
# student1.show_deatils()
# f1 = Faculty("bhadra","cse",university_name="nitw")
# f1.show_deatils()
# print(Student.mro()) ## MRO = method resolution order.

# b1 = B("cse","NITW")
# c1 = C("cye001",'NITW')
# b1.show_deatils()
# print(c1.course)
# print(c1.uni_name)

print(Student.mro())
s1 = Student("jayanth","cse","nitw")
s1.show_deatils()
#print(s1.course)