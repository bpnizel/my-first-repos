# the name of file and the name of class same name 

#  class add new type
class ClassPerson:
    def __init__(self, name, age):
        self._name = name
        self._age = age 
    
    # _height = None # private member
    
    
    def getName(self):
        return self._name 
    
    
    def getAge(self):
        return self._age
    

    def getPersonString(self):
        return "the person " + str(self.getName()) + " is " + str(self.getAge()) + " years old"
    
    def printMySelf(self):
        return self.getPersonString()



# __main__
if __name__ == "__main__":
    test_name = "test_name"
    test_age = 80
    person = ClassPerson(test_name, test_age,) 
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + person.getName())


     