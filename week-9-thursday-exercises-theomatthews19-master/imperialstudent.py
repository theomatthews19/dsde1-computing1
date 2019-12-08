class ImperialStudent:
    def __init__(self, name, CID):
        self.name = name
        self.CID = CID

class DEStudent(ImperialStudent):
    def __init__(self, year, tutor):
        self.year = year
        self.tutor = tutor
    
    def library(self, faculty):
        pass


s1 = ImperialStudent('Santa Claus', 14352617)
print(s1.name, s1.CID)
s1 = DEStudent(1, "Peter Cheung")
print(s1.year, s1.tutor)