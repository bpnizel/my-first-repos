from Class_person import ClassPerson
from Student import Student
from Employee import Employee
 
 

person = ClassPerson("Alex", 30)

student = Student("Alex", 30, "English", 3, 85)
          

employee = Employee("john", 40 , "Software Engineer", 4500)


print(type(employee))


people = [ person, student, employee]
for person in people:
    print(person.printMySelf())  
     