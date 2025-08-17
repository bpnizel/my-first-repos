from Class_person import ClassPerson
from Student import Student
from Employee import Employee
 
 

person = ClassPerson("Alex", 30)

student = Student("mike", 27, "engineer", 3, 70)


print("this is from programmer 2")         

employee = Employee("john", 40 , "Software Engineer", 4500)


print(type(employee))


people = [ person, student, employee]
for person in people:
    print(person.printMySelf())  

     

