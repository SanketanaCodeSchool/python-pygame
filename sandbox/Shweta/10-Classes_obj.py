class Student:
    student_id = 0
    student_name = ""
    phone_no = 0
    address =0

    def display(self):
        print(self.student_id)
        print(self.student_name)
        print(self.phone_no)
        print(self.address)

    def take_input(self):
        self.student_id = int(input("Enter student ID:"))
        self.student_name = input("Enter student name:")
        self.phone_no = int(input("Enter student Phone number:"))
        self.address = input("Enter student Address:")

student1 = Student()
student2 = Student()
student1.take_input()
student2.take_input()
student1.display()
student2.display()

