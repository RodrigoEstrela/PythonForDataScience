from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

print("THIS WILL GIVE AN ERROR")
student = Student(name="Edward", surname="agle", id="toto")
print(student)
