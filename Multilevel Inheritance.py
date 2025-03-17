# Educator class
class Educator:
    def prepareLesson(self):
        print("Creating the lesson with general content")


class ITInstructor(Educator):
    def prepareLesson(self):
        print("Developing the lesson with technical content, concentrating on coding.")

    def teachCoding(self):
        print("Instructing on coding principles and programming languages.")


class DatabaseInstructor(ITInstructor):
    def prepareLesson(self):
        print("Designing the lesson to combine SQL with Python.")

    def teachCoding(self):
        print("Instructing coding, emphasizing the integration of SQL with Python.")

    def demonstrateMySQL(self):
        print("Showcasing MySQL database concepts and query techniques.")


educator = Educator()
educator.prepareLesson() 

it_instructor = ITInstructor()
it_instructor.prepareLesson() 
it_instructor.teachCoding()  
db_instructor = DatabaseInstructor()
db_instructor.prepareLesson()  
db_instructor.teachCoding()  
db_instructor.demonstrateMySQL()  
