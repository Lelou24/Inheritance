class EsportsEvent:
    def __init__(self, event_date):
        self.event_date = event_date 

    def scheduleMatch(self):
        print(f"Scheduling the match for {self.event_date}.")


class StudentDivision(EsportsEvent):
    def registerTeam(self, team_name):
        print(f"Registering the student team: {team_name} for the event.")


class FacultyDivision(EsportsEvent):
    def assignReferee(self, referee_name):
        print(f"Assigning {referee_name} as the match referee.")

# Example Usage
event = EsportsEvent("2025-03-20")
event.scheduleMatch()  

student_division = StudentDivision("2025-03-20")
student_division.scheduleMatch()  
student_division.registerTeam("Team Bah")  

faculty_division = FacultyDivision("2025-03-20")
faculty_division.scheduleMatch() 
faculty_division.assignReferee("Sam Smith")  