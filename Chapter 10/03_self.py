class Employee:
    language = "python" # This is a class attribute.
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "JavaScript" # This is an instance attribute. 
# print(harry.language, harry.salary)
harry.getInfo()
# Employee.getInfo(harry)  # Ye bhi asme thing ko print krega.

