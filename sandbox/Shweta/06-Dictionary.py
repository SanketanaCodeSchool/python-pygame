student = {}

for i in range(2):
    name = input("Enter a student name: ")
    age = int(input("Enter the age of the student: "))
    student[name] = age

print(student)

print(len(student))

if "riya" in student:
    print("riya is there into the dictionary")
else:
    print("Riya doesn't exist in this dictionary")