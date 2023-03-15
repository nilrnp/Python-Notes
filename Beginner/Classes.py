# CLASSES
class Student:
    def __init__(self, name, major, year): # constructor
        self.name = name
        self.major = major
        self.year = year

    def printInfo(self):
        print(self.name, "is a", self.major, "major in his", str(self.year), "year!" )

class Teacher(Student):
    def teaching(self):
        return True

def main():
    Nil = Student("Nil", "CS", 4) # object
    print(Nil.name)
    Nil.printInfo()

    John = Teacher("John","Teacher","7")
    print(John.printInfo())
    print(John.teaching())

main()

