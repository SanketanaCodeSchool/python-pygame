class Student:
    def __init__(self, student_id, student_name, phone_no, address):
        self.student_id=student_id
        self.student_name=student_name 
        self.phone_no=phone_no 
        self.address = address 

    def display(self):
        print(self.student_id)
        print(self.student_name)
        print(self.phone_no)
        print(self.address)

    

student1 = Student(101, "Bob", 123344, "New York")
student2 = Student(102, "John", 345566, "Boston")
student1.display()
student2.display()

