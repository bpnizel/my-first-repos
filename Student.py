from Class_person import ClassPerson

class Student(ClassPerson):
    def __init__(self, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(name, age) #super  אפשר לגשת קלאס האב שמוריש את  התכונות בעזרת
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg 

    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg
    
    def printStudent(self):
        return self.getPersonString() + ", the field of study is " + str(self.getFieldOfStudy()) + ", the year of study is " + str(self.getYearOfStudy()) + ", the avg is  " + str(self.getScoreAvg())
    
    def printMySelf(self):
        return self.printStudent() 


        