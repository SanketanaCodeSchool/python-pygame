#Getters and setter

class student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, new_grade):
        if 0<= new_grade <=100:
            self.__grade = new_grade
        else:
            print("Invalid grade!!!")

    def display_info(self):
        print(f"Student: {self.name}, Grade : {self.__grade}")


s1 = student("Aarav", 89)
print(s1.get_grade())
s1.display_info()

s1.set_grade(92)
s1.display_info()